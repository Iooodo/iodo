# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def bin_func(a):
    b2 = format(a, '#b')
    return b2

c = int(input('Enter number:'))
z = bin_func(c)
decimal_number = eval(z)
print(z, decimal_number)

