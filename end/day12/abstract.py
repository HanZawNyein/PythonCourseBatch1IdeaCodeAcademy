from abc import ABC,abstractmethod

class CreditCard(ABC):
    @abstractmethod
    def get_all_amount(self)->int:
        print("I am from CreditCard.")
        return 100

class User(CreditCard):
    def get_all_amount(self):
        res=super().get_all_amount()
        res*=10
        print("I am from User.")
        print(res)
        return res

if __name__ == "__main__":
    # credit_card = CreditCard()
    # credit_card.get_all_amount()

    user = User()
    user.get_all_amount()