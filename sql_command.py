import mysql.connector
from mysql.connector import Error
from decimal import Decimal
import datetime

db_host = "localhost"
db_username = "root" # replace with your MySQL username
db_password = "rootpassword" # replace with your MySQL password

if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host= db_host,
            user= db_username,  
            password= db_password  
        )
        
        if connection.is_connected():
            print("Connected to MySQL Server")
            cursor = connection.cursor()

            #Create a database
            cursor.execute("CREATE DATABASE IF NOT EXISTS Stock_Management")

            #Use the created database
            cursor.execute("USE Stock_Management")

            #Create a product table
            create_table_query1 = """
                CREATE TABLE ProductStorage (
                    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    ProductName VARCHAR(255) NOT NULL,
                    PricePerUnit DECIMAL(10, 3),
                    Quantity INT NOT NULL,
                    Unit VARCHAR(50),
                    Category VARCHAR(255),
                    Import_Date DATE,
                    Expire_Date DATE,
                    Shelf_Life VARCHAR(60),
                    Supplier VARCHAR(255),
                    Status VARCHAR(50)
                );
            """
            cursor.execute(create_table_query1)

            #Insert data into the product table
            insert_data_query1 = """
            INSERT INTO ProductStorage (ProductName, PricePerUnit, Quantity, Unit, Category, Import_Date, Expire_Date, Shelf_Life, Supplier, Status)
            VALUES
                (1, 'JameDrink', Decimal('3.000'), 1111, '200mL can', 'Solf-drink', datetime.date(2024, 11, 19), datetime.date(2044, 11, 19), '20y-0m-0d', 'DrinksCompanyKH', 'On Ordering')
                (2, 'Marinda', Decimal('0.500'), 50, None, 'Solf-drink', datetime.date(2024, 11, 21), datetime.date(2028, 11, 21), '4y-0m-0d', 'DrinksCompanyKH', 'Out Of Stock'),
                (3, 'Doritos', Decimal('1.000'), 100, None, 'Chips', datetime.date(2024, 11, 21), datetime.date(2026, 11, 21), '2y-0m-0d', 'SnackCompanyKH', 'Out Of Stock') ,
                (4, 'Cheetos', Decimal('1.000'), 50, None, 'Chips', datetime.date(2024, 11, 21), datetime.date(2028, 11, 21), '4y-0m-0d', 'SnackCompanyKH', 'Available')     ,
                (5, 'Lays', Decimal('1.000'), 120, None, 'Chips', datetime.date(2024, 11, 21), datetime.date(2027, 11, 21), '3y-0m-0d', 'SnackCompanyKH', 'Available')       ,
                (6, 'Bartterfylyfhd', Decimal('1.250'), 12, None, 'Ingredient', datetime.date(2024, 11, 21), datetime.date(2027, 11, 21), '3y-0m-0d', 'HomeCooker', 'Available'),
                (7, 'FreshMilk', Decimal('1.500'), 180, None, 'Milk', datetime.date(2024, 11, 21), datetime.date(2027, 11, 21), '3y-0m-0d', 'HomeCooker', 'Available')       ,
                (8, 'CheeseBurger', Decimal('2.000'), 10, None, 'Burger', datetime.date(2024, 11, 21), datetime.date(2026, 11, 21), '2y-0m-0d', 'BurgerGod', 'On Ordering')  ,
                (9, 'SoySource', Decimal('1.000'), 35, None, 'Source', datetime.date(2024, 11, 21), datetime.date(2027, 11, 21), '3y-0m-0d', 'GodsIngredient', 'Out Of Stock'),
                (10, 'SunflowerOil', Decimal('1.000'), 25, None, 'Oil', datetime.date(2024, 11, 21), datetime.date(2027, 11, 21), '3y-0m-0d', 'GodsIngredient', 'Out Of Stock');
            """
            cursor.execute(insert_data_query1)
            connection.commit()


            #Create a user table
            create_table_query2 = """
                CREATE TABLE UserTable (
                    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    UserName VARCHAR(255) NOT NULL,
                    Phone VARCHAR(255),
                    Email VARCHAR(255),
                    BirthDate DATE,
                    Passcode VARCHAR(100),
                    UserRole VARCHAR(100),
                    UserStatus VARCHAR(100)
                );
            """
            cursor.execute(create_table_query2)

            #Insert data into the user table
            insert_data_query2 = """
            INSERT INTO UserTable (UserName, Phone, Email, BirthDate, Passcode, UserRole, UserStatus)
            VALUES ('Admin', None, None, None, 'admin', 'admin', 'Active');
            """
            cursor.execute(insert_data_query2)
            connection.commit()
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
