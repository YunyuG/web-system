from fastapi import APIRouter,Depends

from .models import UserCreate
from dbutil import AsyncSession, get_session

user_router = APIRouter(prefix="/user")

@user_router.post("")
async def create_user(user: UserCreate,session: AsyncSession = Depends(get_session)):
    session.add(user)
    return {"message":"创建成功","user":user.id}

@user_router.get("/{user_id}")
async def get_user(user_id: int,session: AsyncSession = Depends(get_session)):
    # user = await session.get(User,user_id)
    user = await session.query(UserCreate).filter(UserCreate.id == user_id,UserCreate.hasdeleted == False).first()
    if user is None:
        return {"message":"用户不存在"}
    return user

@user_router.delete("/{user_id}")
async def delete_user(user_id: int,session: AsyncSession = Depends(get_session)):
    user = session.get(UserCreate,user_id)
    if user is None:
        return {"message":"用户不存在"}
    user.hasdeleted = True
    return {"message":"删除成功"}

@user_router.put("/{user_id}")
async def update_user(user_id: int,user_select: UserCreate,session: AsyncSession = Depends(get_session)):
    user_select = session.get(UserCreate,user_id)
    if user_select is None:
        return {"message":"用户不存在"}
    user_select.name = user_select.name
    user_select.age = user_select.age
    user_select.email = user_select.email
    return {"message":"更新成功"}
