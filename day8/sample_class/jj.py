from .human import Human

class JJ(Human):
    def __init__(self, name, age, can_swim):
        self.can_swim = can_swim
        super(JJ, self).__init__(name, age)

if __name__ == "__main__":
    jj = JJ(name="JJ",age=2,can_swim=False)