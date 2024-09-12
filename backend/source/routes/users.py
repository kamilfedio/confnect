from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.user import User
from source.database import get_async_session
from source.schemas.user import UserRead, UserUpdate, UserPasswordUpdate
import source.crud.user as user_crud
from source.dependencies.depends import get_current_user
from source.utils.authenticate import verify_password, get_password_hash

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_me(
    user: UserRead = Depends(get_current_user),
) -> UserRead:
    """
        returns current user
    Args:
        user (UserRead, optional): current user data. Defaults to Depends(get_current_user).

    Returns:
        UserRead: user data object
    """
    return user


@router.get("/{id}", response_model=UserRead)
async def get_user_by_id(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> UserRead:
    """
        returns user by id
    Args:
        id (int): user id
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if user doens't exists

    Returns:
        UserRead: user data object
    """
    user: User | None = await user_crud.get_by_id(id, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


@router.patch("/me", response_model=UserRead)
async def update_user(
    model: UserUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> UserRead:
    """
        updata user data
    Args:
        model (UserUpdate): user update object
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Returns:
        UserRead: user data object after changes
    """
    for key, value in model.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    updated_user: User = await user_crud.update(user, session)

    return updated_user


@router.patch("/me/password", response_model=UserRead)
async def update_user_password(
    model: UserPasswordUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> UserRead:
    """
        change user password
    Args:
        model (UserPasswordUpdate): user change password object
        user (User, optional): current user. Defaults to Depends(get_current_user).
        session (AsyncSession, optional): current session. Defaults to Depends(get_async_session).

    Raises:
        HTTPException: if user password is invalid

    Returns:
        UserRead: user data object
    """
    if not verify_password(model.old_password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password"
        )
    hashed_pass = get_password_hash(model.password)
    user.hashed_password = hashed_pass
    updated_user: User = await user_crud.update(user, session)

    return updated_user
