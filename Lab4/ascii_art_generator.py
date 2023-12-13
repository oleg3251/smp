class AsciiArtGenerator:
    def __init__(self, user_input: str, width: int, height: int, alignment: str, color_option: str):
        self.__user_input = user_input
        self.__ascii_chars = ['@', '#', '*', '+', '=', '-', ':', '.', ' ']
        self.__width = width
        self.__height = height
        self.__alignment = alignment
        self.__color_option = color_option

    def set_ascii_chars(self):
        if self.__color_option == "gray":
            self.__ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
        elif self.__color_option == "bw":
            self.__ascii_chars = [' ', '.', ',', '-', ':', ';', '=', '!', '*', '#', '$', '@']

    def generate_ascii_art(self):
        ascii_art = ""
        for i in range(self.__height):
            for j in range(self.__width):
                char_index = int((ord(self.__user_input[(i * self.__width + j) % len(self.__user_input)]) / 255) * (
                        len(self.__ascii_chars) - 1))
                ascii_art += self.__ascii_chars[char_index]
            ascii_art += "\n"
        return ascii_art

    def set_alignment(self):
        if self.__alignment == "center":
            self.__user_input = self.__user_input.center(self.__width)
        elif self.__alignment == "right":
            self.__user_input = self.__user_input.rjust(self.__width)

    def set_color_option(self):
        self.set_ascii_chars()

    def preview_ascii_art(self):
        print(self.generate_ascii_art())
