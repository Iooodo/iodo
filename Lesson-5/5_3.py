# Вывести четные числа от 2 до N по 5 в строку

n = int(input("n="))

for number in range(2, n+1):
    if number % 2 == 0:
        print(number, end=' ' if number % 5 else '\n')
