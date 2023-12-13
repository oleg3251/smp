import logging

import requests
from requests import Response

from Lab7.http_exception import HttpException
from Lab7.http_method_type import HttpMethod


# Represents HTTP client
class HttpClient:

    # Http Client constructor
    def __init__(self, base_url: str):
        logging.info('Initialize http client')
        self.__base_url = base_url

    # Makes get request
    def get(self, url_params: str = None) -> Response:
        return self.__send_request(method_type=HttpMethod.GET, url_params=url_params)

    # Makes post request
    def post(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.POST, url_params=url_params, data=data)

    # Makes put request
    def put(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.PUT, url_params=url_params, data=data)

    # Makes patch request
    def patch(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.PATCH, url_params=url_params, data=data)

    # Makes delete request
    def delete(self, url_params: str = None, data=None) -> Response:
        return self.__send_request(method_type=HttpMethod.DELETE, url_params=url_params, data=data)

    # Handles all requests
    def __send_request(self, method_type: HttpMethod, url_params: str = None, data=None) -> Response:
        logging.info(f'Making {method_type} request with ({url_params}) params')
        request_url = self.__base_url + (url_params or "")

        request_methods = {
            HttpMethod.GET: requests.get,
            HttpMethod.POST: requests.post,
            HttpMethod.PUT: requests.put,
            HttpMethod.PATCH: requests.patch,
            HttpMethod.DELETE: requests.delete,
        }

        if method_type not in request_methods:
            raise ValueError(f"Invalid HttpMethod: {method_type}")

        request_method = request_methods[method_type]
        response = request_method(request_url, data=data)
        if response.ok:
            return response.json()
        raise HttpException(f"Failed to make HTTP request\nHTTP method: {method_type}, Url parameters:{url_params}")
