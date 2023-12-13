from Lab5.cube import Cube
from Lab5.pyramid import Pyramid
from utils import UserInputHelper
from utils.data_saver import FileHandler


class ArtInterface:

    def __init__(self):
        self.__input_helper = UserInputHelper()

    def run(self):
        while True:
            print("Choose options")
            print("1 - Draw 2D cube\n2 - Draw 3D cube\n3 - Draw 2D pyramid\n0 - Stop\n")
            answer = self.__input_helper.get_limited_user_input('', ['1', '2', '3', '0'])
            if answer is '1':
                art = self.__get_2d_cube()
                self.__print_art(art)
            elif answer is '2':
                art = self.__get_3d_cube()
                self.__print_art(art)
            elif answer is '3':
                art = self.__get_pyramid()
                self.__print_art(art)
            else:
                break
            self.__save_option(art)

    def __get_2d_cube(self):
        x = self.__input_helper.get_int_user_input("Enter x:\n")
        y = self.__input_helper.get_int_user_input("Enter y:\n")
        return Cube.create_2d(x, y)

    def __get_3d_cube(self):
        x = self.__input_helper.get_int_user_input("Enter x:\n")
        y = self.__input_helper.get_int_user_input("Enter y:\n")
        z = self.__input_helper.get_int_user_input("Enter z:\n")
        return Cube().build_3d(x, y, z)

    def __get_pyramid(self):
        x = self.__input_helper.get_int_user_input("Enter x:\n")
        y = self.__input_helper.get_int_user_input("Enter y:\n")
        return Pyramid.create_pyramid(x, y)

    # provide option to save object
    def __save_option(self, content):
        answer = self.__input_helper.get_limited_user_input("Do you want to save art?(y,n)\n", ['y', 'n'])
        if answer is 'y':
            file_name = self.__input_helper.get_user_input("Enter file name\n")
            FileHandler().save_to_txt(file_name, content)

    @staticmethod
    def __print_art(art):
        for i in art:
            print(i)
