from utils.dal import *
from models.vacation_model import *

# vacations business logic
class VacationsLogic:

    # ctor - create DAL object:
    def __init__(self):
        self.dal = DAL()

    
    # get all vacations
    def get_all_vacations(self):
        sql = "SELECT * FROM vacations ORDER BY start_date ASC"
        results = self.dal.get_table(sql)
        vacations = VacationModel.dictionaries_to_vacations(results)
        return vacations
    

    # add a new vacation
    def add_vacation(self, vacation):
        sql = "INSERT INTO vacations(country_id, description, start_date, end_date, price, vacation_photo_filename) VALUES(%s, %s, %s, %s, %s, %s)"
        last_inserted_id = self.dal.insert(sql, (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, vacation.vacation_photo_filename))
        return last_inserted_id
    

    # update existing vacation
    def update_vacation(self, vacation):
        sql = "UPDATE vacations SET country_id=%s, description=%s, start_date=%s, end_date=%s, price=%s, vacation_photo_filename=%s WHERE vacation_id=%s"
        row_count = self.dal.update(sql, (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, vacation.vacation_photo_filename, vacation.vacation_id))
        return row_count
    

    # delete existing vacation
    def delete_vacation(self, id):
        sql = "DELETE FROM vacations WHERE vacation_id = %s"
        params = (id, )
        row_count = self.dal.delete(sql, params)
        return row_count


    #  get a vacation by id and return it's VacationModel object
    def get_vacation_by_id(self, vacation_id):
        sql = "SELECT * FROM vacations WHERE vacation_id = %s"
        result = self.dal.get_scalar(sql, (vacation_id, ))
        
        if result:
            return VacationModel(
                vacation_id=result["vacation_id"],
                country_id=result["country_id"],
                description=result["description"],
                start_date=result["start_date"],
                end_date=result["end_date"],
                price=result["price"],
                vacation_photo_filename=result["vacation_photo_filename"]
            )
        else:
            return None


    # Close resources:
    def close(self):
        self.dal.close()                                 