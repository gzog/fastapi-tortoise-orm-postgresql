import jwt
from fastapi import Depends, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException

from app import settings
from app.user.dependencies import get_current_user
from app.user.helpers.security import authenticate_user
from app.user.models import User
from app.user.schemas import Status, UserRequest, UserResponse

router = APIRouter()


@router.get("", response_model=list[UserResponse])
async def get_users() -> list[UserResponse]:
    return await UserResponse.from_queryset(User.all())


@router.post("", response_model=UserResponse)
async def create_user(user_request: UserRequest) -> UserResponse:
    user = await User.create(**user_request.model_dump(exclude_unset=True))
    return await UserResponse.from_tortoise_orm(user)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    return await UserResponse.from_queryset_single(User.get(id=user_id))


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserRequest) -> UserResponse:
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await UserResponse.from_queryset_single(User.get(id=user_id))


@router.delete("/{user_id}", response_model=Status)
async def delete_user(user_id: int) -> Status:
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")


@router.get("/me", response_model=UserResponse)
async def get_session_user(user: UserResponse = Depends(get_current_user)):
    return user


@router.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    user_obj = await UserRequest.from_tortoise_orm(user)

    token = jwt.encode(user_obj.model_dump(), settings.SECRET_KEY)

    return {"access_token": token, "token_type": "bearer"}
