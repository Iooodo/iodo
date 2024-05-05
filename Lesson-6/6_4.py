# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

# list = ['s', {}, 't', '4', [877, 87], '77', 'd']
# list = list(filter(lambda x: x(type(str)), list))
# print(list)

lst = ['s', {}, 't', (8, "99"), '4', [877, 87], '77', 'd']

def filt_lst(x):
    if type(x) is str:
        return x

result = filter(filt_lst, lst)
print(list(result))


