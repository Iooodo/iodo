# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

countries = {
    "Belarus": ["Minsk", "Grodno", "Brest"],
    "England": ["London", "Edinburgh", "Manchester"],
    "Russia": ["Moscow", "St.Peterburg", "Kaliningrad"]
}
city = input('Enter city:')
for country, cities in countries.items():
    if city in cities:
        print(f'{city} is a city in {country}')
        break
else:
    print(f'Country for {city} not found')


