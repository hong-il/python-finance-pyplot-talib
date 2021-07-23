"""
    @ Author    : hong-il
    @ Date      : 2021-07-24
    @ File name : financeDB.py
    @ File path : 
    @ Description : 
"""
import pymysql
import json


class financeDB:
    def __init__(self):
        with open("config.json") as config_file:
            db_info = json.load(config_file)
            self.host = db_info.get("host")
            self.port = db_info.get("port")
            self.user = db_info.get("user")
            self.password = db_info.get("password")
            self.database = db_info.get("database")
            self.charset = db_info.get("charset")
            self.connect_timeout = db_info.get("connect_timeout")

    def get_connection(self):
        connection = self.get_pymysql_connection()
        connection.autocommit = False
        print(f'database connection ok')
        return connection

    def get_pymysql_connection(self):
        database = pymysql
        connection = database.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            connect_timeout=self.connect_timeout
        )
        return connection
