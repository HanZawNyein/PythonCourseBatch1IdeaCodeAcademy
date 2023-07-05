import json 

class User:
    last_id=0
    users =list()

    def __init__(self) -> None:
        self.users=[]
        self.__read_file()

    def read(self):
        return self.users
           
    def insert(self,name,age):
        self.last_id+=1
        data = {'id':self.last_id,'name':name,'age':age}
        self.__file_write(data,last_id=self.last_id)
        return data
    
    def __file_write(self,data,last_id):
        self.users.append(data)
        dd = {"last_id":last_id,"data":self.users}
        with open('db/user.json','w')as f:
            ss = json.dumps(dd)
            f.write(ss)

    def __read_file(self):
         with open('db/user.json','r')as f:
            data = f.read()
            new_dict = json.loads(data)
            # print(new_dict,"*"*10)
            self.last_id = new_dict["last_id"]
            self.users = new_dict["data"]


if __name__ == "__main__":
    user1 = User()
    print(user1.insert(name="KK",age=100))
    all_user_ids = user1.read()
    print(len(all_user_ids))