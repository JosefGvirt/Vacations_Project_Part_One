from logic.likes_logic import *
from logic.users_logic import *
from logic.vacations_logic import *

class LikesFacade:
    
    # initialize ctor for LikesFacade
    def __init__(self):
        self.likes_logic = LikesLogic()

    
    #---------------------------------------------
    
    # add like to likes table
    def add_like_to_vacation(self, user_id, vacation_id):
        
        # Create a UserModel instance for the user
        user = UserModel(user_id=user_id, first_name="", last_name="", email="", password="", role_id=2)

        # Create a VacationModel instance for the vacation
        vacation = VacationModel(vacation_id=vacation_id, country_id="", description="", start_date="", end_date="", price=0, vacation_photo_filename="")

        # Call the add_like function in LikesLogic
        like_id = self.likes_logic.add_like(user, vacation)

        if like_id is not None:
            return "Like added successfully"
        else:
            return "Failed to add like"
        
    # ------------------------------------------

    # remove a like from likes table
    def unlike_vacation(self, user_id, vacation_id):

        # Call the delete_like function in LikesLogic
        row_count = self.likes_logic.delete_like(user_id, vacation_id)

        if row_count == 0:
            return "Like not found or not removed"

        return "Like removed successfully"

    # ----------------------------------------------------------------

    # Close resources:
    def close(self):
        self.likes_logic.close()

    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()