# Дан файл с многострочным текстом, необходимо подсчитать количество букв в каждой строке и результат записать в другой файл в формате:
# 1 строка - N букв
# 2 строка - M букв




counter = 1
with (
    open('file-1', 'r', encoding='utf-8') as file_1,
    open('file-2.txt', 'w', encoding='utf-8') as file_2
):
        for line in file_1:
            file_2.write('{} строка - {} букв\n'.format(counter, len(line)-1))
            counter += 1