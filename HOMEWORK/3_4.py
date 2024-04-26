# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

numbers = [7, 8.0, -878]
pos_count = 0
neg_count = 0
for num in numbers:
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1

print("Positive numbers:", pos_count)
print("Negative numbers:", neg_count)