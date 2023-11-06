import os
from dotenv import load_dotenv

load_dotenv()

CLICKHOUSE_HOST = os.environ.get('CLICKHOUSE_HOST')
CLICKHOUSE_PORT = os.environ.get('CLICKHOUSE_PORT')
CLICKHOUSE_USERNAME = os.environ.get('CLICKHOUSE_USERNAME')
CLICKHOUSE_PASSWORD = os.environ.get('CLICKHOUSE_PASSWORD')
CLICKHOUSE_DB_NAME = os.environ.get('CLICKHOUSE_DB_NAME')
CLICKHOUSE_TABLE_NAME = os.environ.get('CLICKHOUSE_TABLE_NAME')
