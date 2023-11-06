import sys
import os
import clickhouse_connect
from clickhouse_connect.driver.tools import insert_file
from src.config import CLICKHOUSE_HOST, CLICKHOUSE_PORT, CLICKHOUSE_USERNAME, CLICKHOUSE_PASSWORD, CLICKHOUSE_DB_NAME, \
    CLICKHOUSE_TABLE_NAME

### Добавление путей для обособленного запуска скрипта
sys.path.append(os.path.join(os.getcwd(), ' ../..'))


def get_client():
    with clickhouse_connect.get_client(host=CLICKHOUSE_HOST, port=CLICKHOUSE_PORT, username=CLICKHOUSE_USERNAME,
                                       password=CLICKHOUSE_PASSWORD) as client:
        yield client


def create_database():
    client = get_client().__next__()
    client.command(f'DROP DATABASE IF EXISTS {CLICKHOUSE_DB_NAME}')
    client.command(f'CREATE DATABASE {CLICKHOUSE_DB_NAME}')


def create_table():
    client = get_client().__next__()
    client.command(f'DROP TABLE IF EXISTS {CLICKHOUSE_TABLE_NAME}')
    table_statement = f'CREATE TABLE {CLICKHOUSE_TABLE_NAME} (url String, title String, text String, topic String, tags String, date Date) ENGINE MergeTree ORDER BY date'
    client.command(table_statement)


def inserting_data_into_table():
    client = get_client().__next__()
    insert_file(client, CLICKHOUSE_TABLE_NAME, 'data_compressed_copy.csv')
    # insert_file(client, CLICKHOUSE_TABLE_NAME, 'lenta-ru-news.csv')
    print(client.command('SELECT timezone()'))
    print(client.query('SELECT title FROM lenta_table').result_rows)


if __name__ == '__main__':
    create_database()
    create_table()
    inserting_data_into_table()
