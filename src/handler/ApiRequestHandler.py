import logging

import requests


class ApiRequestHandler:

    def __init__(self):
        self.base_url = "base_url"
        self.headers = {'Content-type': 'application/json'}
        self.logger = logging.getLogger(type(self).__name__)
        return

    def callWebService(self, customer_account, product_code):
        request = ApiRequestHandler.createApiRequest(customer_account, product_code)
        response = requests.post(
            self.base_url + "api_endpoint",
            json=request, headers=self.headers)
        return response

    @staticmethod
    def createApiRequest(customer_account, product_code):
        request = {
            'abc': '002',
            'pqr': customer_account[0],
            'wxy': '20190808',
            'xyz': [{'supc': product_code[0], 'mno': 'false'}]
        }

        return request
