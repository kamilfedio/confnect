import json
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exc
from datetime import datetime

from source.models.token import Token
from source.database import get_async_session
from source.schemas.user import UserRead, UserCreate
from source.schemas.utils import EmailSchema, ResetPasswordRequest, ResetPassword
from source.utils.authenticate import (
    get_password_hash,
    create_token,
    authenticate_user,
    verify_refresh_token,
    get_token,
)
from source.config.env_config import host_config
from source.models.user import User
import source.crud.user as user_crud
import source.crud.tokens as tokens_crud
from source.utils.enums import EmailType, TokenType
from source.celery.tasks import send_email_queue

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_create: UserCreate, session: AsyncSession = Depends(get_async_session)
) -> dict[str, str]:
    """
        register user in db
    Args:
        user_create (UserCreate): user data object
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if user already exists

    Returns:
        dict[str, str]: refresh and access tokens
    """
    hashed_pass = get_password_hash(user_create.password)

    user = User(
        **user_create.model_dump(exclude={"password"}), hashed_password=hashed_pass
    )
    try:
        await user_crud.create(user, session)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    access_token: str = await create_token(
        user.id, type=TokenType.ACCESS, session=session
    )
    refresh_token: str = await create_token(
        user.id, type=TokenType.REFRESH, session=session
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    session: AsyncSession = Depends(get_async_session),
) -> dict[str, str]:
    """
        create access token
    Args:
        form_data (OAuth2PasswordRequestForm, optional): login form data. Defaults to Depends(OAuth2PasswordRequestForm).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if incorrected data

    Returns:
        dict[str, str]: refresh and access tokens
    """
    user: UserRead | bool = await authenticate_user(
        form_data.username, form_data.password, session
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token: str = await create_token(
        user.id, type=TokenType.ACCESS, session=session
    )
    refresh_token: str = await create_token(
        user.id, type=TokenType.REFRESH, session=session
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh")
async def refresh_token(
    refresh_token: str, session: AsyncSession = Depends(get_async_session)
) -> dict[str, str]:
    """
        refresh access token
    Args:
        refresh_token (str): refresh token
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if invalid refresh token

    Returns:
        dict[str, str]: access token
    """
    if not await verify_refresh_token(refresh_token, session):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    token: Token | None = await get_token(
        refresh_token, session, token_type=TokenType.REFRESH
    )
    access_token: str = await create_token(
        token.user_id, type=TokenType.ACCESS, session=session
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout(refresh_token: str, session=Depends(get_async_session)) -> Response:
    """
    logout user by disabling refresh token
    Args:
        refresh_token (str): refresh token
        session (_type_, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        Response: status code
    """

    check_token: Token | None = await tokens_crud.get_by_id(
        refresh_token, TokenType.REFRESH, session
    )
    if not check_token:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Token doesn't exists",
        )
    if check_token.expirated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirated"
        )
    await tokens_crud.disable_token(refresh_token, session)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/reset-password")
async def reset_password(
    password_request: ResetPasswordRequest,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    """
    send email with reset password link
    Args:
        password_request (ResetPasswordRequest): request password schema
        background_tasks (BackgroundTasks): background tasks
        session (AsyncSession, optional): db session. Defaults to Depends(get_async_session).

    Returns:
        Response: status code 200
    """

    user_by_email: User | None = await user_crud.get_by_email(
        password_request.email, session
    )
    if not user_by_email:
        return
    
    reset_token: str = await create_token(
        user_by_email.id, session=session, type=TokenType.RESET_PASSWORD
    )
    data_to_send: dict[str, str] = {
        "user_name": user_by_email.first_name,
        "reset_link": f"{host_config.BASE_URL}/change-password/{reset_token}",
        "current_year": str(datetime.now()),
    }
    email_schema: EmailSchema = EmailSchema(
        type=EmailType.RESET_PASSWORD,
        to=password_request.email,
        subject="Hi, Reset your password!",
        content=data_to_send,
    )
    email_schema_dict: dict = email_schema.model_dump()
    email_schema_dict["type"] = email_schema_dict["type"].value
    send_email_queue.delay(json.dumps(email_schema_dict))

    return Response(content="Password reset link sent", status_code=status.HTTP_200_OK)


@router.post("/change-password")
async def change_password_after_reset(
    reset_password: ResetPassword, session: AsyncSession = Depends(get_async_session)
) -> Response:
    """
    confirm password reset with changing it
    Args:
        reset_password (ResetPassword): reset password schema
        session (AsyncSession, optional): db session.
                Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if token doesnt exists
        HTTPException: if token is expirated
        HTTPException: if passwords aren't the same

    Returns:
        Response: status code
    """
    token: Token | None = await get_token(
        reset_password.reset_token, session=session, token_type=TokenType.RESET_PASSWORD
    )
    if not token:
        raise HTTPException(
            detail="Token is incorrect",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    if token.expirated:
        raise HTTPException(
            detail="Token is expirated",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    user: User = token.user
    if not reset_password.new_password == reset_password.confirm_password:
        raise HTTPException(
            detail="Password't are incorrect",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    hashed_pass = get_password_hash(reset_password.new_password)
    user.hashed_password = hashed_pass

    await user_crud.update(user, session=session)
    await tokens_crud.disable_token(token.token, session=session)

    return Response(status_code=status.HTTP_202_ACCEPTED, content="Password reseted")
