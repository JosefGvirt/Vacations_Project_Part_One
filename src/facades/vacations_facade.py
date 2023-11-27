from logic.vacations_logic import *
from datetime import datetime

class VacationsFacade:

    # define ctor
    def __init__(self):
        self.vacations_logic = VacationsLogic()

    # -------------------------------------------------------------------------
    
    # get all vacations in the db ordered by start date ascending
    def get_all_vacations(self):

        # Retrieve all vacations including those completed, ordered by start date ascending
        vacations = self.vacations_logic.get_all_vacations()
        return vacations
    
    
    # -------------------------------------------------------------------------

    # add new vacation to vacations db
    def add_new_vacation(self, country_id, description, start_date, end_date, price, vacation_photo_filename):
        
        # Perform input validation:

        # check if start date and end date are in valid format "%Y-%m-%d"
        if not self.is_valid_date_format(start_date) or not self.is_valid_date_format(end_date):
            return "Invalid date format"

        # check if start date is before end date
        if not self.is_valid_date_range(start_date, end_date):
            return "End date cannot be earlier than start date"

        # check if start date is in the future
        if not self.is_future_date(start_date):
            return "Start date must be a future date"

        # check if vacation price is between 0 to 10k and positive
        if not self.is_valid_price(price):
            return "Invalid price. Price should be between 0 and 10,000"

        # Create a VacationModel instance and add the new vacation to the database
        vacation = VacationModel(
            vacation_id=None,
            country_id=country_id,
            description=description,
            start_date=start_date,
            end_date=end_date,
            price=price,
            vacation_photo_filename= vacation_photo_filename 
        )
        last_inserted_id = self.vacations_logic.add_vacation(vacation)

        return last_inserted_id  # Return the ID of the newly added vacation

    # -------------------------------------------------------------------------

    # update existing vacation
    def update_vacation(self, vacation_id, country_id, description, start_date, end_date, price, vacation_photo_filename=None):

        # Perform input validation
        if not self.is_valid_date_format(start_date) or not self.is_valid_date_format(end_date):
            return "Invalid date format"

        if not self.is_valid_date_range(start_date, end_date):
            return "End date cannot be earlier than start date"

        if not self.is_valid_price(price):
            return "Invalid price. Price should be between 0 and 10,000"

        # Check if vacation_photo_filename is provided, otherwise, keep the existing value
        if vacation_photo_filename is None:
            existing_vacation = self.vacations_logic.get_vacation_by_id(vacation_id)
            if existing_vacation:
                vacation_photo_filename = existing_vacation.vacation_photo_filename

        # Create a VacationModel instance and update the existing vacation in the database
        vacation = VacationModel(
            vacation_id=vacation_id,
            country_id=country_id,
            description=description,
            start_date=start_date,
            end_date=end_date,
            price=price,
            vacation_photo_filename=vacation_photo_filename
        )
        row_count = self.vacations_logic.update_vacation(vacation)

        if row_count == 0:
            return "Vacation not found or not updated"

        return "Vacation updated successfully"
    # -------------------------------------------------------------------------

    # delete an existing vacation 
    def delete_vacation(self, vacation_id):

        # Check if the vacation with the provided ID exists
        existing_vacation = self.vacations_logic.get_vacation_by_id(vacation_id)
        if not existing_vacation:
            return "Vacation not found"

        # Call the delete_vacation function in VacationsLogic
        row_count = self.vacations_logic.delete_vacation(vacation_id)

        if row_count == 0:
            return "Vacation not found or not deleted"

        return "Vacation deleted successfully"
    
    # -------- Helper Functions -------------------------------------------------------------------------

    # check if inserted date is correctly formatted "%Y-%m-%d"
    def is_valid_date_format(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False


    # check if start_date is smaller than end_date (earlier)
    def is_valid_date_range(self, start_date, end_date):
        return start_date <= end_date


    # check if inserted start date is in the future (not past dates)
    def is_future_date(self, date_str):
        return datetime.strptime(date_str, "%Y-%m-%d") > datetime.now()
    

    # check if vacation price is valid (positive and up to 10k)
    def is_valid_price(self, price):
        return 0 <= price <= 10000
    
    # -----------------------------------------------------------------------

    # Close resources:
    def close(self):
        self.vacations_logic.close()

    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
