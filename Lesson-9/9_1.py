# Дан файл с многострочным текстом, необходимо подсчитать количество букв в каждой строке и результат записать в другой файл в формате:
# 1 строка - N букв
# 2 строка - M букв


class TextWriter:

    def writer(self, name_file1: str, name_file2: str):
        counter = 1
        with (
            open(name_file1, 'r', encoding='utf-8') as file_1,
            open(name_file2, 'w', encoding='utf-8') as file_2
        ):
                for line in file_1:
                    file_2.write('{} строка - {} букв\n'.format(counter, len(line)-1))
                    counter += 1

a = TextWriter()
a.writer('file-1', 'file-2.txt')