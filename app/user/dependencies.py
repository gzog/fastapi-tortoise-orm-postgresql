import jwt
from fastapi import Depends, HTTPException, status

from app import settings
from app.user.helpers.security import OAUTH2_SCHEME
from app.user.models import User
from app.user.schemas import UserRequest, UserResponse


async def get_current_user(token: str = Depends(OAUTH2_SCHEME)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user = await User.get(id=payload.get("id"))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return await UserResponse.from_tortoise_orm(user)
