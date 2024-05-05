# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

lst = [4, 5, 7, 3, 787, 22, 32]

def func(l):
    n_1 = [i for i in l if i % 2]
    n_2 = [i for i in l if not i%2]
    return sorted(n_2) + sorted(n_1)
print(func(lst))