import clickhouse_connect
from clickhouse_connect.driver.client import Client
from src.config import CLICKHOUSE_HOST, CLICKHOUSE_PORT, CLICKHOUSE_USERNAME, CLICKHOUSE_PASSWORD


def get_client() -> Client:
    """Создание сессии для подключения к CLickHouse"""
    with clickhouse_connect.get_client(host=CLICKHOUSE_HOST, port=CLICKHOUSE_PORT, username=CLICKHOUSE_USERNAME,
                                       password=CLICKHOUSE_PASSWORD) as client:
        yield client
