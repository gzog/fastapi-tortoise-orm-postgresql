from fastapi import Depends
from fastapi.routing import APIRouter
from passlib.hash import bcrypt
from starlette.exceptions import HTTPException

from app.api.dependencies import get_current_user
from app.repositories.user import UserRepository
from app.models.user import User
from app.schemas.user import UserRequest, UserResponse
from app.schemas.status import Status

router = APIRouter()


@router.get("", response_model=list[UserResponse])
async def get_users() -> list[UserResponse]:
    users = await UserRepository.get_all()
    return users


@router.post("", response_model=UserResponse)
async def create_user(user_request: UserRequest) -> UserResponse:
    user = await UserRepository.create(user_request.model_dump(exclude_unset=True))
    return user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    user = await UserRepository.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserRequest) -> UserResponse:
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await UserResponse.from_queryset_single(User.get(id=user_id))


@router.delete("/{user_id}", responses={204: {"model": None}})
async def delete_user(user_id: int) -> None:
    deleted_count = await UserRepository.delete(user_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
