# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name = "Nadya"
age = 28
city = "Minsk"
print("Hello, %s. You are %d years old too. I'm glad to see you in %s" % (name, age, city))


name = "Nadya"
age = 28
city = "Minsk"
print("Hello, {} You are {} years old too. I'm glad to see you in {}.".format(name, age, city))


name = "Nadya"
age = 28
city = "Minsk"
print(f"Hello, {name} You are {age} years old too. I'm glad to see you in {city}.")