# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError

class Category:
    categories = ['size', 'number']

    @classmethod
    def add(cls, name_category: str):
        if name_category not in cls.categories:
            cls.categories.append(name_category)
        # print(cls.categories.index(name_category))
        else:
            raise ValueError
        print(cls.categories.index(name_category))

    @classmethod
    def get(cls, ind: int):
        if ind in range(len(cls.categories)):
            print(cls.categories[ind])
        else:
            raise IndexError

    @classmethod
    def delete(cls, ind_cat: int):
        if ind_cat in range(len(cls.categories)):
            del cls.categories[ind_cat]

    @classmethod
    def update(cls, ind_cat: int, new_name: str):
        if ind_cat not in range(len(cls.categories)) and new_name not in cls.categories:
            cls.categories.append(new_name)
        else:
            raise ValueError


b = Category()
b.add('color')
c = Category()
c.add('weight')
d = Category()
d.get(3)
g = Category()
g.delete(5)
h = Category
h.update(4, 'material')
m = Category
m.get(4)



