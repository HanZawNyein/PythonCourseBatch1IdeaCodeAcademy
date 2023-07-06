import model

class User(model.Model):
    _name="res.users"


if __name__ == "__main__":
    user = User()
    # print(user.read_all())
    user.insert({"name":"han","age":20})
    print(user.read_all())