from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
from models.books import Model
from routers.books import router as books_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    print("База готова")
    yield
    print("Сервер выключается")

app = FastAPI(lifespan=lifespan)
app.include_router(books_router)