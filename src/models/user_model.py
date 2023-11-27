# User model
class UserModel:

    # constructor - initial data members:
    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id


    # Display the user:
    def display(self):
        print(f"""ID: {self.user_id},\n 
              First Name: {self.first_name},\n 
              Last Name: {self.last_name},\n 
              Email: {self.email},\n
              Password: {self.password},\n
              Role: {self.role_id}\n""")


    # Convert user dictionary to user model:
    @staticmethod
    def dictionary_to_user(dictionary):
        user = UserModel(dictionary["user_id"],
                         dictionary["first_name"],
                         dictionary["last_name"],
                         dictionary["email"],
                         dictionary["password"],
                         dictionary["role_id"])
        return user


    # Convert a list of user dictionaries to list of user models:
    @staticmethod
    def dictionaries_to_users(list_of_dictionaries):
        users = []
        for item in list_of_dictionaries:
            user = UserModel.dictionary_to_user(item)
            users.append(user)
        return users