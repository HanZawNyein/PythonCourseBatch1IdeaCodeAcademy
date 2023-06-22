class Human:
    def __init__(self, name, age):
        print("I am Human")
        self.__name = name
        self.age = age

    def _eating(self):
        print("Human is eating")

if __name__ == "__main__":
    human = Human(name="I am Human", age=0)
