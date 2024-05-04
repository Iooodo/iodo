# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

number_1 = input("Введите число:")
operation = input("Введите знак действия:")
number_2 = input("Введите число:")

try:
    number_1 = float(number_1)
    number_2 = float(number_2)
except ValueError:
    print(f"Введено неверное число")

if operation in ("+", "-", "*", "/"):
    if operation == "+":
        print(number_1 + number_2)
    elif operation == "-":
        print(number_1 - number_2)
    elif operation == "*":
        print(number_1 * number_2)
    elif operation == "/":
        if number_2 != 0:
            print(number_1 / number_2)
        else:
            print("Делить на ноль нельзя!")
else:
        print("Неверный знак!")
