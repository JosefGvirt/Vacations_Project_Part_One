# User model
class VacationModel:

    # constructor - initial data members:
    def __init__(self, vacation_id, country_id, description, start_date, end_date, price, vacation_photo_filename=None):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.vacation_photo_filename = vacation_photo_filename


    # Display the VacationModel:
    def display(self):
        print(f"Vacation ID: {self.vacation_id}, Country: {self.country_id}, Description: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}, Price: {self.price}, Vacation_photo_filename: {self.vacation_photo_filename}")


    # Convert vacation dictionary to vacation model:
    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacation = VacationModel(dictionary["vacation_id"],
                         dictionary["country_id"],
                         dictionary["description"],
                         dictionary["start_date"],
                         dictionary["end_date"],
                         dictionary["price"],
                         dictionary["vacation_photo_filename"])
        return vacation


    # Convert a list of vacation dictionaries to list of vacation models:
    @staticmethod
    def dictionaries_to_vacations(list_of_dictionaries):
        vacations = []
        for item in list_of_dictionaries:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
    

    # in case a print statement is made for the VacationModel object
    def __str__(self):
        return f"Vacation ID: {self.vacation_id}, Country: {self.country_id}, Description: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}, Price: {self.price}, Vacation_photo_filename: {self.vacation_photo_filename}"
