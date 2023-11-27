from logic.users_logic import *
import re

class UsersFacade:

    # initialize ctor
    def __init__(self):
        self.users_logic = UsersLogic()

    #---------------------------------------------

    # helper function to test validity of email address using regex
    def is_valid_email(self, email):

        # Simple email format validation using regular expression
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(email_pattern, email))
    
    #---------------------------------------------

    # sign up new user [email has to be new, password at least 4 char, valid mail]
    def sign_new_user(self, first_name, last_name, email, password):

        # Perform input validation
        if not self.is_valid_email(email):
            return "Invalid email format"
        
        if len(password) < 4:
            return "Password must be at least 4 characters long"
        
        if self.users_logic.is_mail_registered(email):
            return "Email is already registered"

        # Create a UserModel instance and add the user to the database
        user = UserModel(user_id=None, first_name=first_name, last_name=last_name, email=email, password=password, role_id=2)
        last_inserted_id = self.users_logic.add_user(user)

        return last_inserted_id  # Return the ID of the newly added user

    #---------------------------------------------
    
    # sign in existing user [email, password, valid mail, password at least 4 chars long]
    def sign_in(self, email, password):
        
        # Perform input validation
        if not self.is_valid_email(email):
            return "Invalid email format"
        
        if len(password) < 4:
            return "Password must be at least 4 characters long"

        # Check if the user with the provided email and password exists
        user = self.users_logic.get_user_by_credentials(email, password)

        if not isinstance(user, UserModel):
            return "Invalid email or password"

        # Return the user's information if authentication is successful
        return {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role_id": user.role_id
        }

    # -----------------------------------------------------------------------------------

    # Close resources:
    def close(self):
        self.users_logic.close()

    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()

