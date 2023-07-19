import logging
from typing import Dict, List, Any

import psycopg2
import pandas as pd
from psycopg2.extras import execute_batch


class PostgresConnector:
    def __init__(self, host='localhost', database='postgres', user='gbig', password='gbig'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def __enter__(self):
        logging.info('Opening connection.')
        self.conn = psycopg2.connect(
            host=self.host, database=self.database, user=self.user, password=self.password
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        logging.info('Changes has been committed.')
        self.conn.close()
        logging.info('Connection closed.')

    def __read_query_from_file(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf8') as f:
            return ' '.join(f.readlines()).replace('\n', '')

    def insert_batch_data(self, data: List[Dict[str, Any]], table: str, schema: str = 'ecommerce'):
        columns = data[0].keys()
        values = [tuple(d.values()) for d in data]

        placeholders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO {schema}.{table} ({', '.join(columns)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            execute_batch(cur, query, values)
        logging.info(f'Data has been loaded to {table} table with psycopg2.')

    def execute_command_from_file(self, file_path: str) -> int:
        query = self.__read_query_from_file(file_path)
        with self.conn.cursor() as cur:
            cur.execute(query)
        logging.info(
            f'SQL query ({query[:50]}...) has been successfully executed. New row count is: {cur.rowcount}'
        )

    def select(self, file_path: str) -> pd.DataFrame:
        query = self.__read_query_from_file(file_path)
        return pd.read_sql_query(query, self.conn)
