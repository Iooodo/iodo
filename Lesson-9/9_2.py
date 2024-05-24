# Дан CSV файл с колонками: article, name, description, price - описание товаров.
# Необходимо прочитать файл в список словарей с ключами взятых из первой строки
# (названия колонок) без использования встроенной библиотеки CSV


file = open('file.csv', 'r')

file_lines = file.readlines()
file_lines = [line[:-1] for line in file_lines]
file_inf = [line.split(',') for line in file_lines]

dict_list = []
for line in file_inf[1:]:
    dict_from_csv = {}
    for i, v in enumerate(line):
        dict_from_csv[file_inf[0][i]] = v
    dict_list.append(dict_from_csv)
print(dict_list)

file.close()


