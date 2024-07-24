from backend.models import User


async def authenticate_user(username: str, password: str) -> User | bool:
    user = await User.get(username=username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user
