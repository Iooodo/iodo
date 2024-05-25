# Дан CSV файл с колонками: article, name, description, price - описание товаров.
# Необходимо прочитать файл в список словарей с ключами взятых из первой строки
# (названия колонок) без использования встроенной библиотеки CSV


class MakeDictList:

    def __init__(self, name_file: str):
        self.file = open(name_file, 'r')
        self.file_lines = self.file.readlines()
        self.file_lines = [line[:-1] for line in self.file_lines]
        self.file_inf = [line.split(',') for line in self.file_lines]

    def make_dictlst(self):
        dict_list = []
        for line in self.file_inf[1:]:
            dict_from_csv = {}
            for i, v in enumerate(line):
                dict_from_csv[self.file_inf[0][i]] = v
            dict_list.append(dict_from_csv)
        print(dict_list)
        self.file.close()

a = MakeDictList('file.csv')
a.make_dictlst()




