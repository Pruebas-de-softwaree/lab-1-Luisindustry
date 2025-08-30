import time
class UserManager:
    def __init__(self,max_users=1000):
        self.users = []  
        self.max_users = max_users

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = UserManager()
    
     #user_manager.add_user(1,"Luis")
    #user_manager.add_user(2,"Carlos")
    #user_manager.add_user(3,"Perez")

    #print("Usuario:", user_manager.find_user(1))
    #print("Usuario:", user_manager.find_user(2))
    #print("Usuario:", user_manager.find_user(3))
    
    #user_manager.delete_user(1)
    #user_manager.delete_user(2)
    #user_manager.delete_user(3)
    #print(user_manager.users)

    #print(user_manager.get_all_names())

    #print(user_manager.average_user_id())
    #-----------------------------------------------#

    for i in range(3):
       print(user_manager.add_user(i,f"Yo soy el num :{i}")) 
    

    
print("end")