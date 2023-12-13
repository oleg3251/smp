import pyfiglet
from termcolor import colored


class AsciiArtGenerator:
    def __init__(self, font_choice, color_choice, char_choice):
        self.font_choice = font_choice
        self.color_choice = color_choice
        self.char_choice = char_choice

    def generate_art(self, user_input, width, height):
        ascii_art = pyfiglet.figlet_format(user_input, font=self.font_choice)
        colored_ascii_art = colored(ascii_art, color=self.color_choice)

        formatted_ascii_art = ""
        for line in colored_ascii_art.split("\n"):
            formatted_ascii_art += line.center(width).replace(" ", self.char_choice) + "\n"

        formatted_ascii_art *= height

        return formatted_ascii_art
