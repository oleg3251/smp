def calculator():
    while True:
        try:
            # Завдання 1: Введення користувача
            num1 = float(input("введіть перше число: "))
            operator = input("введіть операцію (+, -, *, /, ^, √, %): ")
            num2 = float(input("введіть друге число: "))

            # Завдання 2: Перевірка оператора
            if operator not in ('+', '-', '*', '/', '^', '√', '%'):
                print("помилка: введено недійсний оператор")
                continue

            # Завдання 3: Обчислення
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Завдання 5: Обробка помилок
                if num2 == 0:
                    print("помилка: ділення на нуль.")
                    continue
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == '√':
                result = num1 ** (1 / num2)
            elif operator == '%':
                result = num1 % num2

            print("Результат:", result)

            # Завдання 4: Повторення обчислень
            another = input("бажаєте виконати ще одне обчислення? (так /ні): ")
            if another.lower() != 'так':
                break

        except ValueError:
            print("Помилка: введені дані повинні бути числами.")
        except ZeroDivisionError:
            print("Помилка: ділення на нуль.")
        except Exception as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    calculator()
