from fastapi import FastAPI
from user.api import user_router
from dbutil import create_tables

async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
