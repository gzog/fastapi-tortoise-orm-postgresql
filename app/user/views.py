from fastapi.routing import APIRouter
from starlette.exceptions import HTTPException

from app.user.models import User
from app.user.schemas import Status, UserRequest, UserResponse

router = APIRouter()


@router.get("", response_model=list[UserResponse])
async def get_users():
    return await UserResponse.from_queryset(User.all())


@router.post("", response_model=UserResponse)
async def create_user(user: UserRequest):
    user_obj = await User.create(**user.model_dump(exclude_unset=True))
    return await UserResponse.from_tortoise_orm(user_obj)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    return await UserResponse.from_queryset_single(User.get(id=user_id))


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserRequest):
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await UserResponse.from_queryset_single(User.get(id=user_id))


@router.delete("/{user_id}", response_model=Status)
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
