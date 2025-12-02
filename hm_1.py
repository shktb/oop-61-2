class Car:
    def __init__(self, name, color, year):
        self.year = year
        self.name = name
        self.color = color
        self.petrol = False
        self.movement = False
    def vroom(self):
        return f'Машина рычит "ВРУМ ВРУМ"'
    def opinion(self):
        return f'Друг говорит, что {self.name} идеальный'
    def gas(self, gas=95):
        self.petrol = True
        return f'В {self.name} залит полный бак {gas} бензина.'
    def drive(self):
        status1 = "мчится" if self.petrol else "стоит на месте (залейте бензин)"
        return f'{self.name} {status1}'
    def info(self):
        status2 = "Полный бак" if self.petrol else "Бензина мало"
        return f'Машина марки {self.name}, {self.year} года, цвет: {self.color}, {status2},'

car1 = Car("Lexus", "черный", 2007)
car2 = Car("BMW", "белый", 2023)
car3 = Car("Mercedes", "зеленый", 2020)
print(car1.info())
print(car1.vroom())
print(car1.gas(92))
print(car1.drive())
print(car1.info())

print("\n" + car2.info())
print(car2.drive())
print(car2.gas(98))
print(car2.drive())
print(car2.info())
print(car2.opinion())

print("\n" + car3.info())
print(car3.vroom())
print(car3.opinion())
