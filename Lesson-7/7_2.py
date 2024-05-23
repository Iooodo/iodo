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
        self.cars = [car_1, car_2, car_3, car_4]
    def find_car(self, count_passengers: int, is_baby: bool):
       for car in self.cars:
           if car.count_passenger_seats >= count_passengers and car.is_baby_seat == is_baby and car.is_busy is False:
               print(car)
               car.is_busy = True
               break
           elif car.count_passenger_seats >= count_passengers and is_baby is False and car.is_busy is False:
               print(car)
               car.is_busy = True
               break
       else:
           if car.count_passenger_seats < count_passengers:
               print(None)
           elif car.is_busy is True:
               print(None)


# order1 = Taxi()
# order1.find_car(5, True)
# order2 = Taxi()
# order2.find_car(5, False)
# order3 = Taxi()
# order3.find_car(2, True)
# order4 = Taxi()
# order4.find_car(7, False)
# order5 = Taxi()
# order5.find_car(1, False)
# order6 = Taxi()
# order6.find_car(2, False)

