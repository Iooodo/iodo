# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car:
    color: str
    count_passenger_seats: int
    is_baby_seat: bool
    is_busy: bool

    def __init__(self, color, count_passenger_seats, is_baby_seat):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f'Car information: color - {self.color}, number of passenger seats - {self.count_passenger_seats}, '
                f'baby seat - {self.is_baby_seat}, busy - {self.is_busy}')

car_1 = Car('red', 5, True)
print(car_1)
