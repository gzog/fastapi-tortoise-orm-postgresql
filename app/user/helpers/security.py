from fastapi.security import OAuth2PasswordBearer

from app.user.models import User
from app.user.schemas import UserRequest, UserResponse

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")


async def authenticate_user(username: str, password: str):
    user = await User.get(email=username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user
