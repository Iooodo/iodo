# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None


class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f'Car information: color - {self.color}, number of passenger seats - {self.count_passenger_seats}, '
                f'baby seat - {self.is_baby_seat}, busy - {self.is_busy}')


car_1 = Car('red', 5, True)
car_2 = Car('blue', 2, False)
car_3 = Car('green', 4, True)
car_4 = Car('yellow', 5, False)


class Taxi:
    def __init__(self):
        self.cars = list[Car]
    def find_car(self, count_passengers: int):
       if 


