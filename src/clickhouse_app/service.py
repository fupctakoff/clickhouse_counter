from fastapi import Depends
from fastapi.responses import JSONResponse
from typing import Sequence
from src.clickhouse_app.utils import get_client
from src.config import CLICKHOUSE_TABLE_NAME
from src.clickhouse_app.count_resource import words_counter_top_100


class ClickHouseService:

    def __init__(
            self,
            client: get_client = Depends()
    ) -> None:
        self.client = client

    def get_data_for_counter(self) -> Sequence[Sequence]:
        """Делает запрос в БД и получает строковые представления данных"""
        response_data = self.client.query(f'SELECT title, text, topic FROM {CLICKHOUSE_TABLE_NAME}')
        return response_data.result_rows

    def get_count_words(self) -> JSONResponse:
        """Возвращает список слов и количество этих слов в БД"""
        data = self.get_data_for_counter()
        response = words_counter_top_100(data)
        return JSONResponse(response)
