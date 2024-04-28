# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')
print("Hello, %s. You are %s years old too. I'm glad to see you in %s!" % (name, age, city))


name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')
print("Hello, {}. You are {} years old too. I'm glad to see you in {}!".format(name, age, city))


name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')
print(f"Hello, {name}. You are {age} years old too. I'm glad to see you in {city}!")