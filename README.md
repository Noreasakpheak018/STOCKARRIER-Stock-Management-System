# 📜 STOCKARRIER Overview 📖
## 1. Project title: STOCKARRIER
STOCKARRIER is a combination of the words: 'Stock' and 'Carrier'. 
## 2. Issues and solutions
This application is made to help businesses manage their stocks/inventories. It can be used by any type of business that needs inventory, from small to large corporations. One of the core issues the app aims to solve is assisting small, medium, or family-sized businesses in transformation and digitalization from regular and traditional inventory tracking methods, like using paper to note.
## 3. Current progress
### Problem analysis
Many businesses and corporations use less efficient and slower stock management methods. This can lead to overloading stock or stockouts. Additionally, some businesses are still using the regular method, like noting on paper, to track their storage.
### Design
* Programming language, **Python**, is used in developing this application with some of its libraries, like **tkinter** and **ttkinter** to ensure user-friendly interface, **datetime**, ...,etc. 
* Besides, **MySQL** is used as the database to store product data and user data.
### Enhancement
The app can be used in the real-life management process, but some features could be improved the capability of it, such as:
* **Branches switcher**  to manage storage between branches of the store/mart/inventory
* **Alert system** to warn users about the expired products
* **Users manager**: allowed admin to manipulate users by adding, updating, or removing more effectively
* **Extract data**: provide an option for the user to download the items list, users list, for example: download as an Excel file
## 4. Project Functions/Features
### Product manipulate
* **Insert/Add**: to add a new product to the storage by inputting its information
* **Update**: to update/change the current information of a product
* **Delete**: to delete/remove a product from the storage
* **Search**: to search/filter/find any item by the given input data
* **Display**: display the current products and their information in the table
### User and Account
* **Log-in**: by inputting username and its corresponding password/code
* **Log-out**: logged out of the current user and leave the main page to the log-in page
* **Sign-Up**: register a new user
* **Change password**: allowed a user to change their account's password
### Other features
* **Mode switch**: switch between dark and light mode
* **Note box**: to guide users on how to use the app properly
* **Message box**: to feedback on user action
## 5. Expected number of pages
### Currently available pages (4):
* **Log-in page**: landing page
* **Sign-in page**: to register new user
* **Change password** page
* **Main page**: for managing product inventory
### Upcoming pages:
* **Activity log page**: show all the changes/history
* **User manager page**: for admin uses to manage users (add, delete, update)
* **Extract data page**: for a user to select items in the storage and download
* **Sell-driven inventory update page**: for real-time updates an item's data in the stock triggered by a sale
## 6. Database applied
 Using **MySQL** as database
### Current tables (2):
* **Product table**: stores products' information, such as ID, name, price, quantity, unit, imported date, etc.
* **User table**: stores users' personal information, like name, phone, email, date of birth, password, etc.
### Upcoming tables:
* **Sale table**: stores sold items for later use
* **Supplier table**: stores supplier information, like contract, contact, supplied items, etc.
## 7. Project references
* The design is inspired by **Code First with Hala** (a YouTube channel), video: [Python Excel App - Excel Viewer & Data Entry Form [Tkinter, openpyxl] Python GUI Project](https://youtu.be/8m4uDS_nyCk?si=G0PStO7G0t3XQLad)
* Theme use: from GitHub: [Forest-ttk-theme](https://github.com/rdbende/Forest-ttk-theme)
# 🚀Intruction on how to use the application🏷️
## Required solfware and libraries
* IDE for running Python: PyCharm, Visual Studio Code, etc.
* Install Python
* Install some Python libraries (if not yet installed):
  1. Pillow (PIL): `pip install pillow`
  2. Python-dateutil: `pip install python-dateutil`
* Database: MySQL:
 1. Download and install **MySQL** using this [LINK](https://dev.mysql.com/downloads/installer/)
 2. Install MySQL connector using the command: `pip install mysql-connector-python`
## Set up the application
 1. Go to `sql_command.py` file then change the device (local machine) MySQL information, such as **username**, **password**, and **host**
 2. Run `sql_command.py` file once to set up the database and its tables, then insert default data into the tables (can be deleted after)
 3. After all these steps: the application is ready to be used: `main.py`
  


