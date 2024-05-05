# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def bin_func(a):
    b_num = format(a, '#b')
    return b_num

n = int(input('Enter number:'))
b_number = bin_func(n)
d_number = eval(b_number)
print(b_number, d_number)

