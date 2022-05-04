import requests

from currency.utils import PQConnect
from currency.constants import *


pq_connect = PQConnect(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_DATABASE)


def create_table():
    query = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            currency VARCHAR ( 50 ) NOT NULL,
            date DATE NOT NULL,
            result double precision NOT NULL,
            created_on TIMESTAMP NOT NULL DEFAULT NOW()
        );
        """
    pq_connect.execute_commit(query)


def get_currency():
    url = f'https://api.exchangerate.host/convert?from={FROM}&to={TO}'
    response = requests.get(url)
    data = response.json()
    result = [f"{FROM}-{TO}", data['date'], data['result']]
    return result


def insert_result(result):
    query = f""" INSERT INTO {TABLE_NAME} (currency, date, result) VALUES (%s,%s,%s)"""
    pq_connect.execute_commit(query, result)


def download():
    create_table()  # Можно сделать создание не в коде, чтобы каждый раз не запускалось это во время исполнения дага
    result = get_currency()
    insert_result(result)
