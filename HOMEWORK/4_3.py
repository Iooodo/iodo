# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры


n = int(input("n="))
numbers = [i for i in range(0, n+1)]
dict_my = {k: {"name": input("Enter name: "), "email": input("Enter email: ")} for k in numbers}
print(dict_my)

n = int(input("n="))
dict_my = {}
for i in range(0, n+1):
    dict_my[i] = {"name": input("Enter name: "), "email": input("Enter email: ")}
print(dict_my)