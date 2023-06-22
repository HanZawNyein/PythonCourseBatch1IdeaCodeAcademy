from .human import Human

class Driver(Human):  # subclass
    def __init__(self, name, age, can_drive) -> None:
        self.can_drive = can_drive
        super(Driver, self).__init__(name, age)

    def driving(self):
        if self.can_drive:
            print("driver is driving")
        else:
            print("driver can't drive")

if __name__ == "__main__":
    driver = Driver(name="Mg Mg",age=25,can_drive=True)
    driver.driving()