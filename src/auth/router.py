import fastapi
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth import services, schemas

router = APIRouter(
    prefix='/auth',
    tags=['Auth'])


@router.post('/register')
async def create_user(
        user: schemas.UserCreate,
        session: AsyncSession = Depends(get_async_session)
):
    db_user = await services.get_user_by_email(user.email, session)
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail='Email already in use')

    return await services.create_user(user, session)


@router.post('/token')
async def generate_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    user = await services.authenticate_user(form_data.username, form_data.password, session)

    if not user:
        raise fastapi.HTTPException(status_code=401, detail='Invalid Credentials')

    return await services.create_token(user)


@router.get('/me', response_model=schemas.User)
async def get_user(user: schemas.User = Depends(services.get_current_user)):
    return user
