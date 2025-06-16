# class Car(object):
#     brand = 'Mazda'
#     color = 'Black'
#     max_speed = 100
#     __password = 1234
#
#     def __init__(self, b, m):
#         self.brand = b
#         self.max_speed = m
#
#     def upgrade(self):
#         self.max_speed += 25
#         self.__update_password()
#
#     def pr(self):
#         print(f'Модель: {self.brand}, Цвет: {self.color}, Максимальная скорость {self.max_speed}км/ч, Пароль: {self.__password}')
#
#     def get_password(self):
#         return self.__password
#
#     def __update_password(self):
#         self.__password = 234
#
#
# class BigCar(Car):
#     max_weight = 10
#
#     def __init__(self, b, m, mw):
#         super().__init__(b, m)
#         self.max_weight = mw
#
#
#     def prBigCar(self):
#         print(f'Модель: {self.brand}, Цвет: {self.color}, Максимальная скорость {self.max_speed}км/ч, Максимальный вес {self.max_weight}т')
#
#     def add(self):
#         self.max_weight += 10
#
#
# car = Car('Nissan', 190)
# car.upgrade()
# car.pr()
#
# bigcar = BigCar('Libher', 100, 150)
# bigcar.upgrade()
# bigcar.add()
# bigcar.prBigCar()

class Cassa(object):

    def __init__(self, c=0):
        self.cash = c

    def top_up(self, x):
        if x < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной")
        self.cash += x

    def count_1000(self):
        return self.cash // 1000

    def take_away(self, x):
        if x < 0:
            raise ValueError("Сумма изъятия не может быть отрицательной")
        if x > self.cash:
            raise ValueError("Недостаточно денег в кассе")
        self.cash -= x
        return x

    def pr(self):
        print(self.cash)

cassa = Cassa(100)
cassa.take_away(50)
cassa.top_up(500)
cassa.pr()































