from fastapi import APIRouter, Depends
from src.clickhouse_app.service import ClickHouseService

app = APIRouter()


@app.get("/getWords", status_code=200)
def get_words(response: ClickHouseService = Depends()):
    return response.get_count_words()
