import shelve
from abc import ABC,abstractmethod

class Model(ABC):
    _name = None
    last_id = 0
    
    def __get_dbtable_name(self)->str:
        return self._name.replace('.','_')
    
    def insert(self,data):
        with shelve.open('testDB') as db:
            res_user = db.setdefault(self.__get_dbtable_name(),list()).copy()
            if res_user:
                self.last_id = res_user[-1]["id"]
            res_user.append({"id":self.last_id+1,**data})
            db[self.__get_dbtable_name()] = res_user
        return {"id":self.last_id+1,**data}
    
    def read_all(self):
        with shelve.open('testDB') as db:
            result = db.get(self.__get_dbtable_name(),[])
        return result

if __name__ == "__main__":
    model = Model()
    model._name = "test"
    print(model.insert({"name":"Han","age":20}))
    print(model.read_all())