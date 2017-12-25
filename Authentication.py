from LoginDatabase import *

class User:
    database = Database()
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    @staticmethod
    def sign_up(name, password, password2, email):
        if (password != password2):
            return False

        elif (len(password) < 6):
            return False

        else:
            User.database.sign_up(name, password, email)
            return User(name, email)

    @staticmethod
    def login(name, password):
        user_infos = User.database.login(name, password)
        if user_infos != None:
            return User(user_infos[0], user_infos[1])
        else:
            return None