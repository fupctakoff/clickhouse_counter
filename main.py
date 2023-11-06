from fastapi import FastAPI
from src.clickhouse_app.routers import app as clickhouse_router

app = FastAPI()

app.include_router(clickhouse_router)
