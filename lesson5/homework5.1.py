class Cars:
    def __init__(self, make, color):
        self.make = make
        self.color = color

#
class GermanyCars(Cars):
    def __init__(self, make, color, max_speed):
        super().__init__(make, color)
        self.max_speed = max_speed
    def testing(self):
        return "I like high speed"
    # pass

class MunichCars(GermanyCars):
    def __init__(self, make, color, max_speed, high):
        super().__init__(make, color, max_speed)
        self.__high = high

    def get_high(self):
        return self.__high

    def set_high(self, high):
        self.__high = high


munichCars = MunichCars("Germany", "blue", 100, 20)
print(munichCars.make)
print(munichCars.color)
print(munichCars.max_speed)
# print(munichCars.__high)
print(munichCars.get_high())
print(type(munichCars))
print(munichCars.__dict__) # просим распечатать все, касающееся этого класса

class AmericanCars(Cars):
    def __init__(self, make, color, max_speed):
        super().__init__(make, color)
        self.max_speed = max_speed

    def testing(self):
        return "a like high speed"


american_cars1 = AmericanCars("Cadillac", "white", 200)

print(american_cars1.make)
print(american_cars1.color)
print(american_cars1.max_speed)
print(american_cars1.testing())


germany_cars1 = GermanyCars("BMW", "red", 300)

print(germany_cars1.make)
print(germany_cars1.color)
print(germany_cars1.max_speed)
print(germany_cars1.testing())

car1 = Cars("Lada", "red")
print(car1.make)
print(car1.color)

car2 = Cars("Volga", "yellow")
print(car2.make)
print(car2.color)