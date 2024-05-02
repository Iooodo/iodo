# Вывести первые N чисел кратные M и больше K
# n=5 m=2 k=2           2 4 6 8 10

# n = int(input("n="))
# m = int(input("m="))
# k = int(input("k="))
#
# for number in range(n+1):
#     if number % m == 0 and number > k:
#         print(number)
K +=1
while N:
    if not K % M:
        print(K)
        N -= 1
        K += M
    else:
        K += 1