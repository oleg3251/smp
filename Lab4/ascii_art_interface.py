from Lab4.ascii_art_generator import AsciiArtGenerator
from utils import UserInputHelper
from utils.data_saver import FileHandler


class ConsoleInterface:
    @staticmethod
    def __get_user_input() -> str:
        return UserInputHelper.get_user_input("Введіть слово або фразу, яку хочете перетворити в ASCII-арт: ")

    @staticmethod
    def __get_size() -> tuple[int, int]:
        width = UserInputHelper.get_int_user_input("Введіть ширину ASCII-арту: ")
        height = UserInputHelper.get_int_user_input("Введіть висоту ASCII-арту: ")
        return width, height

    @staticmethod
    def __get_alignment() -> str:
        return UserInputHelper.get_limited_user_input("Введіть вирівнювання тексту (left, center, right): ",
                                                      ["left", "center", "right"])

    @staticmethod
    def __get_color_option() -> str:
        return UserInputHelper.get_limited_user_input("Виберіть опцію кольорів (bw, gray): ", ["bw", "gray"])

    @staticmethod
    def run_program():
        while True:
            print("1. Створити ASCII-арт")
            print("2. Попередній перегляд ASCII-арту")
            print("3. Вийти з програми")
            choice = UserInputHelper.get_limited_user_input("Виберіть опцію: ", ["1", "2", "3"])
            if choice == "1":
                user_input = ConsoleInterface.__get_user_input()
                width, height = ConsoleInterface.__get_size()
                alignment = ConsoleInterface.__get_alignment()
                color_option = ConsoleInterface.__get_color_option()
                generator = AsciiArtGenerator(user_input, width, height, alignment, color_option)
                generator.set_alignment()
                print(generator.generate_ascii_art())
                ConsoleInterface.__save_in_file(generator.generate_ascii_art())
                generator.set_color_option()
            elif choice == "2":
                user_input = ConsoleInterface.__get_user_input()
                width, height = ConsoleInterface.__get_size()
                alignment = ConsoleInterface.__get_alignment()
                color_option = ConsoleInterface.__get_color_option()
                generator = AsciiArtGenerator(user_input, width, height, alignment, color_option)
                generator.set_alignment()
                generator.preview_ascii_art()
            elif choice == "3":
                break

    @staticmethod
    def __save_in_file(data):
        is_save = UserInputHelper.get_limited_user_input("Do you want to save it?(y/n)\n", ['y', 'n'])
        if is_save == 'y':
            file_name = UserInputHelper.get_user_input("Enter file name:\n")
            FileHandler.save_to_txt(file_name, data)