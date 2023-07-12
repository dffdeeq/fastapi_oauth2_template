import fastapi
from fastapi import Depends, security
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import jwt as _jwt

from src import config
import passlib.hash as _hash

from src.auth import models, schemas
from src.database import get_async_session


oauth2schema = security.OAuth2PasswordBearer(tokenUrl='/auth/token')


async def get_user_by_email(email: str, session: AsyncSession):
    query = select(models.User).where(models.User.email == email)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    return user


async def create_user(user: schemas.UserCreate, session: AsyncSession):
    user_obj = models.User(email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password))
    session.add(user_obj)
    await session.commit()
    await session.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, session: AsyncSession):
    user = await get_user_by_email(email=email, session=session)

    if not user:
        return False
    if not user.verify_password(password):
        return False

    return user


async def create_token(user: models.User):
    user_obj = schemas.User.model_validate(user)
    token = _jwt.encode(user_obj.model_dump(), config.settings.JWT_SECRET)

    return dict(access_token=token, token_type='bearer')


async def get_current_user(
        session: AsyncSession = Depends(get_async_session),
        token: str = Depends(oauth2schema)
):
    try:
        payload = _jwt.decode(token, config.settings.JWT_SECRET, algorithms=['HS256'])
        user_query = select(models.User).where(models.User.id == payload['id'])
        result = await session.execute(user_query)
        user = result.scalar_one()
    except Exception as e:
        print(f'auth/services/get_current_user(token={token}): {e}')
        raise fastapi.HTTPException(status_code=401, detail='Invalid Email or Password')

    return schemas.User.model_validate(user)
