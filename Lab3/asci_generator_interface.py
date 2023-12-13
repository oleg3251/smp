import pyfiglet

from Lab3.asci_generator import AsciiArtGenerator
from utils import UserInputHelper
from utils.data_saver import FileHandler


class AsciiGeneratorInterface:
    def __init__(self):
        self.__font_list = pyfiglet.FigletFont.getFonts()
        self.__color_list = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        self.__font_choice = ""
        self.__color_choice = ""
        self.__width = 0
        self.__height = 0
        self.__char_choice = ""

    def __get_user_input(self):
        print("ASCII Art Generator")
        print("-------------------")
        user_input = UserInputHelper.get_user_input("Enter a word or phrase to convert to ASCII art: ")

        self.__font_choice = UserInputHelper.get_limited_user_input(
            "Choose a font from the list below:\n{}\n".format(", ".join(self.__font_list)), self.__font_list)

        self.__color_choice = UserInputHelper.get_limited_user_input(
            "Choose a color for the text ({})".format(", ".join(self.__color_list)), self.__color_list)

        self.__width = UserInputHelper.get_int_user_input("Enter the width of the ASCII art: ")
        self.__height = UserInputHelper.get_int_user_input("Enter the height of the ASCII art: ")
        self.__char_choice = UserInputHelper.get_user_input("Enter a character to use for the ASCII art: ")

        return user_input

    @staticmethod
    def __save_ascii_art(ascii_art):
        filename = UserInputHelper.get_user_input("Enter a filename to save the ASCII art: ")
        FileHandler().save_to_txt(filename, ascii_art)

    def run(self):
        user_input = self.__get_user_input()

        ascii_art_generator = AsciiArtGenerator(self.__font_choice, self.__color_choice, self.__char_choice)
        ascii_art = ascii_art_generator.generate_art(user_input, self.__width, self.__height)

        print("Preview:")
        print(ascii_art)

        self.__save_ascii_art(ascii_art)
