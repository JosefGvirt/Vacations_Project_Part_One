from utils.dal import *
from models.user_model import *

# Users business logic:
class UsersLogic:

    # ctor - create a DAL object:
    def __init__(self):
        self.dal = DAL()
    
    
    # add new user (only user NOT ADMIN)
    def add_user(self, user):
        sql = "INSERT INTO users(first_name, last_name, email, password, role_id) VALUES(%s, %s, %s, %s, 2)"
        last_inserted_id = self.dal.insert(sql, (user.first_name, user.last_name, user.email, user.password))
        return last_inserted_id
    

    # get user details by credentials (email and password)
    def get_user_by_credentials(self, user_email, user_password):
        result = self.dal.execute_stored_procedure("get_user_by_credentials", (user_email, user_password))
        user = UserModel.dictionaries_to_users(result)
        if len(user) == 0:
            return f'User {user_email} wasn\'t found'
        return user[0]
    

    # Get a boolean result True if user with mail exists, or False if he doesn't exist
    def is_mail_registered(self, user_email):
        sql = "SELECT * FROM users WHERE users.email = %s"
        result = self.dal.get_scalar(sql, (user_email, ))
        if result == None: # no user with provided mail was found
            return False
        return True # user with provided mail was found


    # Close resources:
    def close(self):
        self.dal.close()