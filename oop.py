
class vehicle:
    def __init__(self,wheels):
        self.wheels = wheels


class Car(vehicle):

    def __init__(self,color,wheels):
        super().__init__(wheels)
        self.color = color
    def drive(self):
        print("this car is already moving")

car = Car(4,'red')
print(car.color)
print(car.drive())

class Phone:
    def __init__(self,color):
        self.color = color

    def is_ringing(self):
        print("this phone is ringing")


phone1 = Phone("black")
print(f"this phone is {phone1.color}")
print(phone1.is_ringing())



class Book:
    def __init__(self,book_type):
        self.book_type = book_type

    def type(self):
        if self.book_type == "exercise book":
            print("you can read and write on this book")
        else:
            print("you can only read on this book")


book1 = Book("exercise book")
print(book1.type())





class Animals:
    def __init__(self, eat, legs):
        self.legs = legs
        self.__owner = "farmer"
        self.eat = eat

        if eat == "cud":
            print("This animal eats cud")
        else:
            print("This animal doesn't chew cud")

    def status(self):
        print("This animal is alive")

    def show_legs(self):
        print(f"This animal has {self.legs} legs")

    def get_owner(self):
        return self.__owner 


class Rabbit(Animals):
    def __init__(self, legs, color, eat):
        self.color = color
        super().__init__(eat, legs)  

    def run(self):
        print("This rabbit is running")

    def sleep(self):
        print("This rabbit is sleeping")



rabbit = Rabbit(4, "black", "cerials")


print(f"Rabbit color: {rabbit.color}")
rabbit.run()
rabbit.sleep()
rabbit.status()
rabbit.show_legs()
print(f"Owner: {rabbit.get_owner()}")



