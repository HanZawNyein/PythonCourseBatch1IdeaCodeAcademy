class Human:
    def __init__(self, name, age) -> None:
        # print("Class is init...")
        # print(name, age)
        self.name = name
        self.age = age

    def eat(self):
        # print(self.name,self.age)
        print(f"{self.name} is eating...")


#

class Driver(Human):

    def __init__(self, name, age, can_drive):
        super(Driver, self).__init__(name, age)
        self.can_drive = can_drive

    def driving(self):
        if self.can_drive:
            print(f"{self.name} is driving ...")
        else:
            print(f"{self.name}'s can't drive")


#
# class Doctor(Driver):
#     def watching(self):
#         print(f"{self.name}'s is watching")
#
# human = Human(name="Human",age=20)
# human.eat()
#
# driver = Driver(name="Driver",age=25)
# driver.eat()
# driver.driving()
#
# doctor = Doctor(name="Doctor", age=100)
# doctor.eat()
# doctor.driving()
# doctor.watching()
#
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def what_is_your_name(tester):
#         print(tester.name)


human = Driver(name="HZN",age=20,can_drive=False)
human.driving()
