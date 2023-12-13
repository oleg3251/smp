import logging

from colorama import Fore

from Lab7.user_repo import UserRepository
from utils import UserInputHelper, DisplayHelper
from utils.data_saver import FileHandler


# Represents user interface
class UsersInterface:

    # User interface constructor
    def __init__(self):
        logging.info('initialize user interface')
        self.__user_repo = UserRepository()
        self.__display_helper = DisplayHelper()
        self.__data_saver = FileHandler()
        self.__colors = {
            '1': Fore.RED,
            '2': Fore.GREEN,
            '3': Fore.YELLOW
        }

    # Runs user interface
    def run(self):
        logging.info('Running user interface')
        while True:
            option = UserInputHelper.get_limited_user_input(
                "Enter option:\n1-Print users\n2-Save users in file\n0-Exit\n",
                ['1', '2', '0'])
            if option == '1':
                self.__display_users()
            elif option == '2':
                self.__save_to_file()
            else:
                break

    # Saves data to file
    def __save_to_file(self):
        logging.info('Saving data to file')
        data = self.__user_repo.get_all_users()
        file_option = UserInputHelper.get_limited_user_input("Enter file type to save(json, csv, txt)\n",
                                                             ['json', 'csv', 'txt'])
        file_name = UserInputHelper.get_user_input("Enter file name\n")
        if file_option == 'json':
            self.__data_saver.save_to_json(file_name, data)
        elif file_option == 'csv':
            self.__data_saver.save_to_csv(file_name, data)
        elif file_option == 'txt':
            self.__data_saver.save_to_csv(file_name, data)

    # Displays users
    def __display_users(self):
        logging.info('Displaying users')
        color = self.__get_color()
        input_option = UserInputHelper.get_limited_user_input("How do you want to display user:\n1 - List\n2 - Table\n",
                                                              ['1', '2'])
        users = self.__user_repo.get_all_users()
        if input_option == '1':
            self.__display_helper.display_list(color, users)
        elif input_option == '2':
            headers = [Fore.RESET + color + "First name",
                       Fore.RESET + color + "Last name",
                       Fore.RESET + color + "Email"]
            rows = [(color + user['firstname'], color + user['lastname'], color + user['email'])
                    for user in users]
            self.__display_helper.display_table(headers, rows)

    # Gets color
    def __get_color(self):
        logging.info('Getting color')
        color = UserInputHelper.get_limited_user_input("Choose color:\n1-Red\n2-Green\n3-Yellow\n",
                                                       list(self.__colors.keys()))
        return self.__colors[color]
