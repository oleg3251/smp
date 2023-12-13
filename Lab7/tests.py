import unittest
from unittest.mock import patch

from Lab7.user_repo import UserRepository
from utils import FileHandler


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.__user_repository = UserRepository()
        self.__file_handler = FileHandler()

    @patch('Lab7.HttpClient')
    def test_get_all_users(self, mock_http_client):
        expected_result = self.__file_handler.read_json_from_file('test_data/users.json')
        mock_http_client.return_value.get.return_value = expected_result

        result = self.__user_repository.get_all_users()

        mock_http_client.assert_called_with(UserRepository.BASE_URL)
        mock_http_client.return_value.get.assert_called_with('/users')
        self.assertEqual(result, expected_result)

    @patch('Lab7.HttpClient')
    def test_get_user_by_id(self, mock_http_client):
        user_id = 1
        expected_result = self.__file_handler.read_json_from_file('test_data/user.json')
        mock_http_client.return_value.get.return_value = expected_result

        result = self.__user_repository.get_user_by_id(user_id)

        mock_http_client.assert_called_with(UserRepository.BASE_URL)
        mock_http_client.return_value.get.assert_called_with(f'/users/{user_id}')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
