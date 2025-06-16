class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def mashina(self):
        print(f'{self.name} Скорость {self.max_speed} Пробег {self.mileage} ')

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}:  {capacity} пассажиров"

class Autobus(Transport):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def mashina2(self):
        print(self.seating_capacity())


autobus = Autobus('Renault Logan', 180, 12)
autobus.mashina()
autobus.mashina2()



