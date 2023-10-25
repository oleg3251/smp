import pyfiglet  # Завдання 2: Інтеграція бібліотеки ASCII-арту
from termcolor import colored  # Завдання 4: Колір тексту

class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.font = "standard"  # Завдання 3: Вибір шрифту
        self.color = "red"
        self.width = 80
        self.height = 10

    def get_user_input(self):
        self.text = input("Введіть текст для ASCII-арту: ")
        self.font = input("Виберіть шрифт (standard, banner, ...) [standard]: ") or "standard"
        self.color = input("Виберіть колір тексту (red, blue, green, ...) [red]: ") or "red"
        self.width = int(input("Введіть ширину ASCII-арту [80]: ") or 80)
        self.height = int(input("Введіть висоту ASCII-арту [10]: ") or 10)

    def generate_ascii_art(self):
        ascii_art = pyfiglet.figlet_format(self.text, font=self.font)
        colored_ascii_art = colored(ascii_art, color=self.color)
        return colored_ascii_art

    def preview_ascii_art(self, ascii_art):
        print("ASCII Art Preview:")
        print(ascii_art)

    def save_to_file(self, ascii_art):
        file_name = input("Введіть ім'я файлу для збереження ASCII-арту: ")
        with open(file_name, "w") as file:
            file.write(ascii_art)

    def run(self):
        self.get_user_input()
        ascii_art = self.generate_ascii_art()
        self.preview_ascii_art(ascii_art)
        self.save_to_file(ascii_art)

if __name__ == "__main__":
    generator = ASCIIArtGenerator()
    generator.run()
