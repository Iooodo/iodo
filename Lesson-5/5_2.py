# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

number_1 = input("Введите число:")
operation = input("Введите знак действия:")
number_2 = input("Введите число:")

if number_1.isdigit():
    number_1 = float(number_1)
else:
    print("Введено неверное число!")
    exit()

if number_2.isdigit():
    number_2 = float(number_2)
else:
    print("Введено неверное число!")
    exit()

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
