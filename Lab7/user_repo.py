import logging

from Lab7.http_client import HttpClient


# Represents users repository
class UserRepository:
    BASE_URL = 'https://jsonplaceholder.org'

    # User repo constructor
    def __init__(self):
        logging.info('Initialize user constructor')
        self.__http_client = HttpClient(UserRepository.BASE_URL)

    # Gets all users
    def get_all_users(self):
        logging.info('Getting all users')
        return self.__http_client.get('/users')

    # Gets user by id
    def get_user_by_id(self, user_id: int):
        logging.info('Getting user by id')
        return self.__http_client.get(f'/users/{user_id}')

    # Creates user
    def create_user(self, user):
        logging.info('Creating user')
        return self.__http_client.post('/users', data=user)
