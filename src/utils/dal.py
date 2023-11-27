import mysql.connector # pip install mysql-connector-python

# Data Access Layer
class DAL:

    # constructor - creating a connection
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost", user= "root", password="", database="vacations"
        )
    
    
    # get back an entire table as a list of dictionaries
    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table
        

    # get back a scalar dictionary
    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
            return scalar
        

    # adding a new row:
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            last_row_id = cursor.lastrowid
            return last_row_id
        

    # updating existing row:
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count
        

    # Deleting existing row:
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()
            row_count = cursor.rowcount
            return row_count
    

    # Executing stored procedure and retrieving results:
    def execute_stored_procedure(self, procedure_name, params=None):
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.callproc(procedure_name, params)
                result = next(cursor.stored_results(), None)
                table = result.fetchall()
                return table
            

    # Close the connection:
    def close(self):
         self.connection.close()