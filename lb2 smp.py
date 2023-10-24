class Calculator:
    def __init__(self):
        # Завдання 2: Ініціалізація калькулятора
        self.result = 0

    def get_user_input(self):
        # Завдання 3: Введення користувача
        self.num1 = float(input("Введіть перше число: "))
        self.operator = input("Введіть операцію (+, -, *, /, ^, √, %): ")
        self.num2 = float(input("Введіть друге число: "))

    def check_operator(self):
        # Завдання 4: Перевірка оператора
        if self.operator not in ('+', '-', '*', '/', '^', '√', '%'):
            print("Помилка: Введено недійсний оператор.")
            return False
        return True

    def calculate(self):
        # Завдання 5: Обчислення
        if self.operator == '+':
            self.result = self.num1 + self.num2
        elif self.operator == '-':
            self.result = self.num1 - self.num2
        elif self.operator == '*':
            self.result = self.num1 * self.num2
        elif self.operator == '/':
            # Завдання 6: Обробка помилок
            if self.num2 == 0:
                print("Помилка: Ділення на нуль.")
                return
            self.result = self.num1 / self.num2
        elif self.operator == '^':
            self.result = self.num1 ** self.num2
        elif self.operator == '√':
            self.result = self.num1 ** (1 / self.num2)
        elif self.operator == '%':
            self.result = self.num1 % self.num2

    def repeat_calculation(self):
        # Завдання 7: Повторення обчислень
        another = input("Виконати ще одне обчислення? (так/ні): ")
        return another.lower() == 'так'

    def run(self):
        while True:
            self.get_user_input()
            if not self.check_operator():
                continue
            self.calculate()
            print("Результат:", self.result)

            if not self.repeat_calculation():
                break

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
