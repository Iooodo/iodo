# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input("Enter your text:")
num_let = {i:text.count(i) for i in text}
print(num_let)