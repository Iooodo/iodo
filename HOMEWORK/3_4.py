# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

number_1 = int(input('Enter number_1: '))
number_2 = int(input('Enter number_2: '))
number_3 = int(input('Enter number_3: '))
number_4 = 0
compare = (bool(number_1 > number_4), bool(number_2 > number_4), bool(number_3 > number_4))
compare_text = str(compare)
print("Negative numbers:", compare_text.count("Fal"))
print("Positive numbers:", compare_text.count("Tru"))
