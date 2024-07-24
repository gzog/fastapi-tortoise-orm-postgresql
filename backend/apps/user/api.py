from fastapi.routing import APIRouter
from starlette.exceptions import HTTPException

from backend.repositories.user import UserRepository
from .schemas import UserUpdateRequest, UserCreateRequest, UserResponse

router = APIRouter()


@router.get("", response_model=list[UserResponse])
async def get_users() -> list[UserResponse]:
    users = await UserRepository.get_all()
    return users


@router.post("", response_model=UserResponse)
async def create_user(request: UserCreateRequest) -> UserResponse:
    user = await UserRepository.create(request.model_dump(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")
    return user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    user = await UserRepository.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, request: UserUpdateRequest) -> UserResponse:
    user = await UserRepository.update(user_id, request.model_dump(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@router.delete("/{user_id}", responses={204: {"model": None}})
async def delete_user(user_id: int) -> None:
    deleted_count = await UserRepository.delete(user_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
