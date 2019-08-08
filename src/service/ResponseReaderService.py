import logging
import time

from src.dao.DataExtractingDao import DataExtractingDao
from src.handler.ApiRequestHandler import ApiRequestHandler


class ResponseReaderService:

    def __init__(self):
        self.data_extracting_dao = DataExtractingDao()
        self.request_handler = ApiRequestHandler()
        self.logger = logging.getLogger(type(self).__name__)
        return

    def extractProductData(self):
        product_list = self.data_extracting_dao.retrieveProductList()
        #product_list = list(dict.fromkeys(product_list))
        return product_list

    def extractCustomerData(self):
        customer_list = self.data_extracting_dao.retrieveCustomerList()
        #customer_list = list(dict.fromkeys(customer_list))
        return customer_list

    def filterResponses(self):
        product_list = self.extractProductData()
        customer_list = self.extractCustomerData()
        request_count = min(len(customer_list), len(product_list))

        for i in range(1, request_count):
            response = self.request_handler.callWebService(customer_list[i], product_list[i]).json()
            request_status = response.get('requestStatuses')
            product_status = response.get('products')[0].get('statuses')

            if request_status is not None:
                print(request_status, product_status, customer_list[i][0], product_list[i][0])
            elif len(product_status) > 0:
                print(request_status, product_status, customer_list[i][0], product_list[i][0])
