import logging

from src.dao.connector.DatabaseConnector import DatabaseConnector


class DataExtractingDao:

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.database_connector = DatabaseConnector()
        self.database_connection = self.database_connector.getConnection()
        return

    def retrieveProductList(self):
        supc_selecting_query = "Select supc from sales_history"
        cursor = self.database_connection.cursor()
        cursor.execute(supc_selecting_query)
        product_list = []
        for (supc) in cursor:
            product_list.append(supc)
        cursor.close()
        return product_list

    def retrieveCustomerList(self):
        customer_list = []
        customer_jo_selecting_query = "Select account_number from sales_history"
        cursor = self.database_connection.cursor()
        cursor.execute(customer_jo_selecting_query)

        for (account_number) in cursor:
            customer_list.append(account_number)
        cursor.close()

        # customer_jx_selecting_query = "Select account_number from customer_jx"
        # cursor = self.database_connection.cursor()
        # cursor.execute(customer_jx_selecting_query)
        #
        # for (account_number) in cursor:
        #     customer_list.append(account_number)
        # cursor.close()

        return customer_list

    def closeConnection(self):
        self.database_connection.close()
