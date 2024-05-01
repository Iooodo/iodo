# Вывести первые N чисел кратные M и больше K

n = int(input("n="))
m = int(input("m="))
k = int(input("k="))

for number in range(n+1):
    if number % m == 0 and number > k:
        print(number)