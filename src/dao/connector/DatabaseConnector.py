import logging

import mysql.connector


class DatabaseConnector:
    def __init__(self):
        self.database_connection = None
        self.logger = logging.getLogger(type(self).__name__)

    def getConnection(self):
        connection_url = "db_url"
        username = "user_name"
        password = "password"
        database = "database"

        database_configuration = {
            'user': username,
            'password': password,
            'host': connection_url,
            'database': database,
            'port': 3306,
            'raise_on_warnings': True
        }

        try:
            self.database_connection = mysql.connector.connect(**database_configuration)
        except:
            self.logger.error("error creating connecting to the database")
            raise Exception("error creating connection to the database")

        return self.database_connection

    def closeConnection(self):
        self.database_connection.close()
