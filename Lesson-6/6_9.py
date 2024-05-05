# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

members = {
    "000123": dict([("name", "Nadya"), ("s_name", "Iodo"), ("phone_number", "+296680968"), ("email", "iodonadin@mail.ru")]),
    "000124": dict([("name", "Katya"), ("s_name", "Kurts"), ("phone_number", "+296201029"), ("email", "")]),
    "000125": dict([("name", "Nastya"), ("s_name", "Dashko"), ("phone_number", "+293201888"), ("adres", "iodonadin@mail.ru")])
}
city_input = "email"

for country, towns in members.items():
    if city_input in towns and city_input is not None:
        print(f'{towns} .')
