from fastapi import APIRouter, Depends

from source.dependencies.depends import get_current_user
from source.schemas.user import UserRead
from source.models.user import User

router = APIRouter()


@router.get("/", response_model=UserRead)
async def test(user: User = Depends(get_current_user)) -> UserRead:
    """
        testing route
    Args:
        user (User, optional): current user. Defaults to Depends(get_current_user).

    Returns:
        UserRead: user data object
    """
    return user
