#Пользователь вводит 3 числа, найти среднее арифмитическое с
#точность 3

number_1 = int(input('Enter number: '))
number_2 = int(input('Enter number: '))
number_3 = int(input('Enter number: '))
sum_numbers = number_1 + number_2 + number_3               #7
numbers = ('number_1', 'number_2', 'number_3')
amt_numbers = len(numbers)
print(round((sum_numbers / amt_numbers), 3))

