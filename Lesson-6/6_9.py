# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

persons = {
    "000123": dict([("name", "Nadya"), ("s_name", "Iodo"), ("phone_number", "+296680968"), ("email", "iodonadin@mail.ru")]),
    "000124": dict([("name", "Katya"), ("s_name", "Kurts"), ("phone_number", "+296201029"), ("email", "")]),
    "000125": dict([("name", "Nastya"), ("s_name", "Dashko"), ("phone_number", "+293201888"), ("city", "Minsk")])
}

values = list(persons.values())

def no_em(l):
    for person, inf in enumerate(l):
        if inf.get('email', '') == '':
            print(inf.get('name'))

no_em(values)