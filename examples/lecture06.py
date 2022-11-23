# lecture 6

class Vehicle:
    def __init__(self, brand):
        self._brand = brand

    def get_brand(self):
        return self._brand

    def __str__(self):
        return 'brand: ' + self._brand


class Car(Vehicle):
    def __init__(self, brand, acceleration):
        Vehicle.__init__(self, brand)
        self._acceleration = acceleration

    def __str__(self):
        return super().__str__() + ', acceleration:' + str(self._acceleration)

class Electric(Vehicle):
    def __init__(self, brand, range):
        Vehicle.__init__(self, brand)
        self._range = range

    def __str__(self):
        return super().__str__() + ', range:' + str(self._range)


class ElectricCar(Car, Electric):
    def __init__(self, brand, acceleration, range):
        super().__init__(brand, acceleration)
        self._range = range


if __name__ == '__main__':
    a = Vehicle('Airbus')
    print(a)
    s = Car('Saab 900', 10.2)
    print(s)
    b = Electric('Brompton', 60)
    print(b)
    t = ElectricCar('Tesla', 5.3, 354)
    print(t)

    


