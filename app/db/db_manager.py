import psycopg2
import psycopg2.extras as extra
from app import app


class DBConnection:
    def __init__(self):
        self.con = psycopg2.connect(
            database="store_manager", user="postgres", password="araali", host="localhost", port="5432")
        self.con.autocommit = True
        self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)

    def create_tables(self):
        queries = (
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                contact VARCHAR(50) NOT NULL,
                role VARCHAR(10) NOT NULL,
                password VARCHAR(25) NOT NULL
            )
            """,

            """
			CREATE TABLE IF NOT EXISTS products (
				product_id SERIAL PRIMARY KEY,
					product VARCHAR(50) NOT NULL,
					quantity INTEGER NOT NULL,
					unit_price INTEGER NOT NULL,
                    reg_date timestamp NOT NULL
							
						)
					"""
            # ,

            # """
            # CREATE TABLE IF NOT EXISTS sales (
            #     sale_id SERIAL PRIMARY KEY,
            #     product VARCHAR(50) NOT NULL,
            #     quantity INTEGER NOT NULL,
            #     amount INTEGER NOT NULL,
            #     attendant VARCHAR(50) NOT NULL,
            #     date timestamp NOT NULL
            # )
            # """
        )
        for query in queries:
            self.dict_cursor.execute(query)

    def delete_test_tables(self):

        delete_queries = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,

            """
			DROP TABLE IF EXISTS products CASCADE
						""",

            """
            DROP TABLE IF EXISTS sales CASCADE
            """
        )
        for query in delete_queries:
            self.dict_cursor.execute(query)
