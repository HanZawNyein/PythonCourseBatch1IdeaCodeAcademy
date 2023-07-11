

class User(Model):
    _name="res.users"


    
    
if __name__ == "__main__":
    user = User()
    print(user.read_all())
    # print(user.insert({"name":"han Zaw","age":20}))

    # base
    # user = Model()
    # user_id = user.insert(data={"name":"Han","age":20})
    # all_user = user.read_all()
    # for _ in all_user:
    #     print(_)
    # print(len(all_user))
