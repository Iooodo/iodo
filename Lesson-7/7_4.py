# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError

class Category:
    categories = [{'name': 'size', 'is_published': False}, {'name': 'number', 'is_published': False}]

    @classmethod
    def add(cls, name_category: str):
        if name_category not in cls.categories:
            new_cat = {'name': name_category, 'is_published': False}
            cls.categories.append(new_cat)
        # print(cls.categories.index(name_category))
        else:
            raise ValueError
        print(cls.categories)


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
            new_cat = {'name': new_name, 'is_published': False}
            cls.categories.append(new_cat)
        else:
            raise ValueError

    @classmethod
    def make_published(cls, ind_cat: int):
        if ind_cat in range(len(cls.categories)):
            category = cls.categories[ind_cat]
            for k, v in category.items():
                if k == 'is_published':
                    is_published = True
                    category[k] = is_published
        else:
            raise IndexError

        print(cls.categories)

    @classmethod
    def make_unpublished(cls, ind_cat: int):
        if ind_cat in range(len(cls.categories)):
            category = cls.categories[ind_cat]
            for k, v in category.items():
                if k == 'is_published':
                    is_published = False
                    category[k] = is_published
        else:
            raise IndexError

        print(cls.categories)

a = Category()
a.make_published(0)
b = Category()
b.make_unpublished(0)