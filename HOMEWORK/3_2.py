#Пользователь вводит 3 числа, найти среднее арифмитическое с
#точность 3

number1 = int(input('Enter number: '))
number2 = int(input('Enter number: '))
number3 = int(input('Enter number: '))
sum_numbers = number1 + number2 + number3               #7
numbers = ('number1', 'number2', 'number3')
amt_numbers = len(numbers)
print(round((sum_numbers / amt_numbers), 3))

