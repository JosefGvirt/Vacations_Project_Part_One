from facades.likes_facade import *
from facades.vacations_facade import *
from facades.users_facade import *
from colorama import *
import random
import string

# Create a test class for testing facades
class Test:

    def __init__(self):

        # Initialize instances of facades
        self.vacations_facade = VacationsFacade()
        self.users_facade = UsersFacade()
        self.likes_facade = LikesFacade()


    # Test functions for VacationsFacade
    # ----------------------------------------------------------------

    # test get_all_vacations() ✅
    def test_vacations_facade_get_all_vacations(self):
        with VacationsFacade() as vacations_facade:
            try:
                print(Fore.CYAN + "results for get_all_vacations():\n" + Style.RESET_ALL )

                # Test get_all_vacations ordered by start date ascending ✅
                vacations = vacations_facade.get_all_vacations()
                print("---")

                for vacation in vacations:
                    vacation.display()
                    print("---")
            except Exception as e:
                print(f"Error in vacations_facade.get_all_vacations: {str(e)}")


    # ----------------------------------------------------------------
    # test add_new_vacation ✅
    def test_vacations_facade_add_new_vacation(self):
        with VacationsFacade() as vacations_facade:
            try:

                try:
                    print(f"{Fore.CYAN} tests for add_new_vacation():{Style.RESET_ALL}\n")

                    # test 1 - add new vacation successful ✅
                    result = vacations_facade.add_new_vacation(
                        country_id= random.randint(1, 11),
                        description= self.get_random_string(30),
                        start_date= "2024-06-01",
                        end_date= "2024-08-31",
                        price= 2000,
                        vacation_photo_filename="test_all().jpg"
                    )
                    print(f"{Fore.GREEN} test 1 [all values are within range, all attributes provided]:{Style.RESET_ALL} {result}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [all values are within range, all attributes provided]:{Style.RESET_ALL} {str(err)}")

                try:
                    # test 2 - photo attr is missing
                    result_two = vacations_facade.add_new_vacation(
                        country_id= 2,
                        description= "Summer in the USA",
                        start_date= "2024-06-01",
                        end_date= "2024-08-31",
                        price= 2000
                    )
                    print(f"{Fore.GREEN} test 2 [photo attribute is missing]:{Style.RESET_ALL} {result_two}")
                except Exception as arr:
                    print(f"{Fore.GREEN} test 2 [photo attribute is missing]:{Style.RESET_ALL} {str(arr)}")

                try:
                    # test 3 - price outside 0-10k range
                    result_three = vacations_facade.add_new_vacation(
                        country_id= 2,
                        description= "Summer in the USA",
                        start_date= "2024-06-01",
                        end_date= "2024-08-31",
                        price= -2000,
                        vacation_photo_filename="summer_in_USA.jpg"
                    )
                    print(f"{Fore.GREEN} test 3 [price outside range 0-10k]:{Style.RESET_ALL} {result_three}")
                except Exception as arr:
                    print(f"{Fore.GREEN} test 3 [price outside range 0-10k]:{Style.RESET_ALL} {str(arr)}")

                try:
                    # test 4 - start_date after end_date
                    result_four = vacations_facade.add_new_vacation(
                        country_id= 2,
                        description= "Summer in the USA",
                        start_date= "2024-08-31",
                        end_date= "2024-06-01",
                        price= 2000,
                        vacation_photo_filename="summer_in_USA.jpg"
                    )
                    print(f"{Fore.GREEN} test 4 [start_date after end_date]:{Style.RESET_ALL} {result_four}")
                except Exception as arr:
                    print(f"{Fore.GREEN} test 4 [start_date after end_date]:{Style.RESET_ALL} {str(arr)}")

                try:
                    # test 5 - choose past dates
                    result_five = vacations_facade.add_new_vacation(
                        country_id= 2,
                        description= "Summer in the USA",
                        start_date= "2023-04-01",
                        end_date= "2023-04-25",
                        price= 2000,
                        vacation_photo_filename="summer_in_USA.jpg"
                    )
                    print(f"{Fore.GREEN} test 5 [choose past dates]:{Style.RESET_ALL} {result_five}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 5 [choose past dates]:{Style.RESET_ALL} {str(err)}")

            except Exception as e:
                print(f"Error in vacations_facade.add_new_vacation: {str(e)}")

    # ------------------------------------------------------------------------------------

    # test update_vacation ✅
    def test_vacations_facade_update_vacation(self):
        with VacationsFacade() as vacations_facade:
            try:
                
                print(f"{Fore.CYAN} tests for update_vacation():{Style.RESET_ALL}\n")

                try:
                    # test 1 - update successful - without photo_filename provided
                    result = vacations_facade.update_vacation(
                        vacation_id=19,
                        country_id=11,
                        description=self.get_random_string(15),
                        start_date="2024-02-11",
                        end_date="2024-02-25",
                        price=2000
                    )
                    print(f"{Fore.GREEN} test 1 [all mandatory attributes provided, except for photo filename ]: {Style.RESET_ALL} {result}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [all mandatory attributes provided, except for photo filename ]: {Style.RESET_ALL} {str(err)}")


                try:
                    # test 2 - update successful with photo_filename provided
                    result_two = vacations_facade.update_vacation(
                        vacation_id=1,
                        country_id=10,
                        description=self.get_random_string(20),
                        start_date="2024-02-11",
                        end_date="2024-02-25",
                        price=1000,
                        vacation_photo_filename="western_wall_trip.jpg"
                    )
                    print(f"{Fore.GREEN} test 2 [all mandatory attributes provided, including photo filename ]: {Style.RESET_ALL} {result_two}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 2 [all mandatory attributes provided, including photo filename ]: {Style.RESET_ALL} {str(err)}")


                try:
                    # test 3 - price outside 0-10k range
                    result_three = vacations_facade.update_vacation(
                        vacation_id=1,
                        country_id=1,
                        description="Trip across the Western Wall in Jerusalem and more",
                        start_date="2024-02-11",
                        end_date="2024-02-25",
                        price=-2000,
                        vacation_photo_filename="western_wall_trip.jpg"
                    )
                    print(f"{Fore.GREEN} test 3 [price outside 0-10k range]: {Style.RESET_ALL} {result_three}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 3 [price outside 0-10k range]: {Style.RESET_ALL} {str(err)}")

                try:
                    # test 4 - start date after end date
                    result_four = vacations_facade.update_vacation(
                        vacation_id=19,
                        country_id=11,
                        description="Trip across the Western Wall in Jerusalem and more",
                        start_date="2024-02-25",
                        end_date="2024-02-14",
                        price=1000,
                        vacation_photo_filename="western_wall_trip.jpg"
                    )
                    print(f"{Fore.GREEN} test 4 [start_date after end_date]: {Style.RESET_ALL} {result_four}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 4 [start_date after end_date]: {Style.RESET_ALL} {str(err)}")

                try:
                    # test 5 - edit past vacation 
                    result_five = vacations_facade.update_vacation(
                        vacation_id=18,
                        country_id=1,
                        description=self.get_random_string(30),
                        start_date="2023-02-11",
                        end_date="2023-02-25",
                        price=1000,
                        vacation_photo_filename="haifa_trip.jpg"
                    )
                    print(f"{Fore.GREEN} test 5 [edit past vacation]: {Style.RESET_ALL} {result_five}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 5 [edit past vacation]: {Style.RESET_ALL} {str(err)}")

            except Exception as e:
                print(f"Error in vacations_facade.update_vacation: {str(e)}")

    # ------------------------------------------------------------------------------------

    # test delete_vacation ✅
    def test_vacations_facade_delete_vacation(self):
        with VacationsFacade() as vacations_facade:
            try:

                print(f"{Fore.CYAN} tests delete_vacation():{Style.RESET_ALL}\n")

                try:
                    # test 1 - delete successful
                    result = vacations_facade.delete_vacation(vacation_id=self.get_random_vacation_id())
                    print(f"{Fore.GREEN} test 1 [delete successful + cascade successful]: {Style.RESET_ALL} {result}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [delete successful + cascade successful]: {Style.RESET_ALL} {str(err)}")

                try:
                    # test 2 - delete unsuccessful - vacation id doesn't exist
                    result_two = vacations_facade.delete_vacation(vacation_id=15)
                    print(f"{Fore.GREEN} test 2 [delete unsuccessful - vacation that doesn't exist]: {Style.RESET_ALL} {result_two}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 2 [delete unsuccessful - vacation that doesn't exist]: {Style.RESET_ALL} {str(err)}")

            except Exception as e:
                print(f"Error in vacations_facade.delete_vacation: {str(e)}")


    # Test functions for UsersFacade
    # ----------------------------------------------------------------

    # test sign_new_user ✅
    def test_users_facade_sign_new_user(self):
        with UsersFacade() as users_facade:

            try:
                print(f"{Fore.CYAN} tests for sign_new_user():{Style.RESET_ALL}\n")

                try:
                    # test 1 - add successfully new user, all attr provided and within constraints
                    result = users_facade.sign_new_user(
                        first_name="Test" + ' ' + self.get_random_string(10),
                        last_name="User",
                        email=self.get_random_mail(),
                        password="password"
                    )
                    print(f"{Fore.GREEN} test 1 [new user added]:{Style.RESET_ALL} {result}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [new user added]:{Style.RESET_ALL} {str(err)}")

                try:
                    # test 2 - email already exists
                    result_two = users_facade.sign_new_user(
                        first_name="Ugi",
                        last_name="Fletzet",
                        email="test_user@example.com",
                        password="password"
                    )
                    print(f"{Fore.GREEN} test 2 [email already exists]:{Style.RESET_ALL} {result_two}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 2 [email already exists]:{Style.RESET_ALL} {str(err)}")

                try:
                    # test 3 - one of attr wasn't provided [last_name]
                    result_three = users_facade.sign_new_user(
                        first_name="Bart",
                        email="test_user_three@example.com",
                        password="password"
                    )
                    print(f"{Fore.GREEN} test 3 [one of attr wasn't provided - last_name]:{Style.RESET_ALL} {result_three}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 3 [one of attr wasn't provided - last_name]:{Style.RESET_ALL} {str(err)}")

                try:
                    # test 4 - email isn't valid
                    result_four = users_facade.sign_new_user(
                        first_name="Bart",
                        last_name="Simpson",
                        email="test_user_twoexample.com",
                        password="password"
                    )
                    print(f"{Fore.GREEN} test 4 [email isn't valid]:{Style.RESET_ALL} {result_four}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 4 [email isn't valid]:{Style.RESET_ALL} {str(err)}")

                try:
                    # test 5 - password len < 4
                    result_five = users_facade.sign_new_user(
                        first_name="Bart",
                        last_name="Simpson",
                        email="test_user_four@example.com",
                        password="hi"
                    )
                    print(f"{Fore.GREEN} test 5 [password length < 4]:{Style.RESET_ALL} {result_five}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 5 [password length < 4]:{Style.RESET_ALL} {str(err)}")

            except Exception as e:
                print(f"Error in users_facade.sign_new_user: {str(e)}")

    # ----------------------------------------------------------------

    # test sign_in ✅
    def test_users_facade_sign_in(self):
        with UsersFacade() as users_facade:

            try:
                print(f"{Fore.CYAN} tests for sign_in():{Style.RESET_ALL}\n")

                try:
                    # test 1 - sign-in successful
                    result = users_facade.sign_in(
                        email="ugi@example.com",
                        password="password"
                    )
                    print(f"{Fore.GREEN} test 1 [success sign in]: {Style.RESET_ALL} {result}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [success sign in]: {Style.RESET_ALL} {str(err)}")

                try:
                    # test 2 - attr missing (password)
                    result_two = users_facade.sign_in(
                        email="ugi@example.com",
                    )
                    print(f"{Fore.GREEN} test 2 [attribute missing- password]: {Style.RESET_ALL} {result_two}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 2 [attribute missing- password]: {Style.RESET_ALL} {str(err)}")


                try:
                    # test 3 - email isn't valid
                    result_three = users_facade.sign_in(
                        email="ugiexample.com",
                        password="password"
                    )
                    print(f"{Fore.GREEN} test 3 [email invalid]: {Style.RESET_ALL} {result_three}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 3 [email invalid]: {Style.RESET_ALL} {str(err)}")

                
                try:
                    # test 4 - password length < 4 chars
                    result_four = users_facade.sign_in(
                        email="ugi@example.com",
                        password="pas"
                    )
                    print(f"{Fore.GREEN} test 4 [password len < 4]: {Style.RESET_ALL} {result_four}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 4 [password len < 4]: {Style.RESET_ALL} {str(err)}")


            except Exception as e:
                print(f"Error in users_facade.sign_in: {str(e)}")


    # Test functions for LikesFacade
    # ----------------------------------------------------------------

    # test add_like_to_vacation ✅
    def test_likes_facade_add_like_to_vacation(self):
        with LikesFacade() as likes_facade:

            try:
                print(f"{Fore.CYAN} tests for add_like_to_vacation():{Style.RESET_ALL}\n")

                try:
                    # test 1 - add successful
                    result = likes_facade.add_like_to_vacation(user_id=random.randint(1, 11), vacation_id=self.get_random_vacation_id())
                    print(f"{Fore.GREEN} test 1 [like added successfully]:{Style.RESET_ALL} {result}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [like added successfully]:{Style.RESET_ALL} {str(err)}")


                try:
                    # test 2 - one of id's doesn't exist
                    result_two = likes_facade.add_like_to_vacation(user_id=10, vacation_id=1)
                    print(f"{Fore.GREEN} test 2 [one of id's doesn't exist]:{Style.RESET_ALL} {result_two}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 2 [one of id's doesn't exist]:{Style.RESET_ALL} {str(err)}")

                try:
                    # test 3 - one attr wasn't specified (user_id)
                    result_three = likes_facade.add_like_to_vacation(vacation_id=1)
                    print(f"{Fore.GREEN} test 3 [attr (user_id) wasn't specified]:{Style.RESET_ALL} {result_three}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 3 [attr (user_id) wasn't specified]:{Style.RESET_ALL} {str(err)}")

            except Exception as e:
                print(f"Error in likes_facade.add_like_to_vacation: {str(e)}")

    # ----------------------------------------------------------------

    # test unlike_vacation ✅
    def test_likes_facade_unlike_vacation(self):
        with LikesFacade() as likes_facade:

            try:
                print(f"{Fore.CYAN} tests for unlike_vacation():{Style.RESET_ALL}\n")

                try:
                    # test 1 - unlike successful
                    likes_user_ids = self.get_all_likes_user_ids()  
                    likes_table_rows = len(likes_user_ids)
                    random_index = random.randint(0, likes_table_rows - 1)
                    
                    # Call the methods and use the result
                    user_id = likes_user_ids[random_index]  
                    vacation_id = self.get_all_likes_vacation_ids()[random_index] 

                    result = likes_facade.unlike_vacation(user_id=user_id, vacation_id=vacation_id)
                    print(f"{Fore.GREEN} test 1 [unlike successful]:{Style.RESET_ALL} {result}")

                except Exception as err:
                    print(f"{Fore.GREEN} test 1 [unlike successful]:{Style.RESET_ALL} {str(err)}")


                try:
                    # test 2 - unlike unsuccessful - likes don't exist
                    result_two = likes_facade.unlike_vacation(user_id=20, vacation_id=5)
                    print(f"{Fore.GREEN} test 2 [unlike unsuccessful, row doesn't exist]:{Style.RESET_ALL} {result_two}")
                except Exception as err:
                    print(f"{Fore.GREEN} test 2 [unlike unsuccessful, row doesn't exist]:{Style.RESET_ALL} {str(err)}")

            except Exception as e:
                print(f"Error in likes_facade.unlike_vacation: {str(e)}")
    # ----------------------------------------------------------------
    # helper functions

    # create a random string of text
    def get_random_string(self, length):

        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    

    # get all vacation id's in a list
    def get_all_vacation_ids(self):
        self = DAL()
        sql = "SELECT vacation_id FROM vacations"
        results = self.get_table(sql)
        vacation_id_list = []
        for object in results:
            vacation_id_list.append(object['vacation_id'])

        self.close()
        return vacation_id_list
    

    # get a random id from vacation table
    def get_random_vacation_id(self):
        id_list = self.get_all_vacation_ids()
        return random.choice(id_list)
    

    # return a random mail address
    def get_random_mail(self):
        text = self.get_random_string(10)
        return text + '@example.com'
    

    # get all likes user_id's in a list
    def get_all_likes_user_ids(self):
        self = DAL()
        sql = "SELECT * FROM likes"
        results = self.get_table(sql)
        likes_user_id_list = []
        for object in results:
            likes_user_id_list.append(object['user_id'])

        self.close()
        return likes_user_id_list
    
    
    # get all likes vacation_id's in a list
    def get_all_likes_vacation_ids(self):
        self = DAL()
        sql = "SELECT * FROM likes"
        results = self.get_table(sql)
        likes_vacation_id_list = []
        for object in results:
            likes_vacation_id_list.append(object['vacation_id'])

        self.close()
        return likes_vacation_id_list


    # Run all test functions
    def test_all(self):
       
        # -------------------------------------------------------

        # Block to test VacationsFacade functions
        print(Fore.BLUE + "Testing VacationsFacade:\n" + Style.RESET_ALL)

        self.test_vacations_facade_get_all_vacations() # test get_all_vacations() ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)

        self.test_vacations_facade_add_new_vacation() # test add_new_vacation() ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)

        self.test_vacations_facade_update_vacation() # test update_vacation() ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)

        self.test_vacations_facade_delete_vacation() # test delete_vacation() ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)
        
        # -------------------------------------------------------
        
        # Block to test UsersFacade functions
        print(Fore.BLUE + "Testing UsersFacade:\n" + Style.RESET_ALL)

        self.test_users_facade_sign_new_user() # test sign_new_user() ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)

        self.test_users_facade_sign_in() # test sign_in() ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)

        # -------------------------------------------------------

        # Block to test LikesFacade functions
        print(Fore.BLUE + "Testing LikesFacade:\n" + Style.RESET_ALL)

        self.test_likes_facade_add_like_to_vacation() # test add_like_to_vacation ✅
        print(Fore.YELLOW + "\n--- Divider ----\n" + Style.RESET_ALL)
        
        self.test_likes_facade_unlike_vacation() # test unlike_vacation ✅
        print(Fore.YELLOW + "\n--- Divider ----\n")
        print(Style.RESET_ALL)


    # Implement the __enter__ method (does nothing)
    def __enter__(self):
        return self

    # Implement the __exit__ method (does nothing)
    def __exit__(self, exc_type, exc_value, traceback):
        pass