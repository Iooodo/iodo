# Вывести первые N чисел кратные M и больше K
# n=5 m=2 k=2           2 4 6 8 10

n = int(input("n="))
m = int(input("m="))
k = int(input("k="))

k +=1
while n:
    if not k % m:
        print(k)
        n -= 1
        k += m
    else:
        k += 1