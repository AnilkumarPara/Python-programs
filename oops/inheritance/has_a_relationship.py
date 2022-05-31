class Sunil:
    bike=1
    def has_bike(self):
        print("Sunil has bike and drive the bike")

class Anil:
    s=Sunil()
    car=1
    def has_car(self):
        print("Anil has Car and drive the car")

a=Anil()
a.s.has_bike()
Anil.s.has_bike()
