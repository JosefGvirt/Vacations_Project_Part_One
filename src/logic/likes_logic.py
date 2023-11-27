from utils.dal import *

# class likes business logic:
class LikesLogic:

    # create a DAL object:
    def __init__(self):
        self.dal = DAL()


    # add like to vacation
    def add_like(self, user, vacation):
        sql = "INSERT INTO likes(user_id, vacation_id) VALUES(%s, %s)"
        last_inserted_id = self.dal.insert(sql, (user.user_id, vacation.vacation_id))
        return last_inserted_id
    

    # delete like from vacation
    def delete_like(self, user_id, vacation_id):
        sql = "DELETE FROM likes WHERE user_id = %s AND vacation_id= %s"
        params = (user_id, vacation_id)
        row_count = self.dal.delete(sql, params)
        return row_count
    

    # Close resources:
    def close(self):
        self.dal.close()  