# STOCKARRIER-Stock-Management-System Overview
## 1. Project title: STOCKARRIER
STOCKARRIER is a combination of the words: 'Stock' and 'Carrier'. 
## 2. Issues and solutions
This application is made to help businesses in mamnaging their stocks/inventories. It can be used in any types of business that needed the use of inventory, from small to large scale corporations. One of the core issues to be solved by the app is to assist small, medium, or family size businesses in transformation and digitalization from regular and traditional inventory tracking method, like using papers to note.
## 3. Current progress
### Problem analysis
Stock management methods in many businesses/corporations are less efficient and slower in manipulating. This can lead to overloading stock or stockout. Additionally, some businesses are still using the regular method, like noting on papers, to track their storage.
### Design
Programming language, **Python**, is used in developing this application with some of its libraries, like **tkinter** and **ttkinter** to ensure user-friendly interface, **datetime**, ... . 
Besides, **MySQL** is used as the database to store products data and also users data.
### Enhancement
The app can be used in read-life management process, but there are some features can could improve the capability of it, such as:
* **Branches switcher**  to manage stroages between branches of the store/mart/inventory
* **Alert system** to warn users about the expired products
* **Users manager**: allowed admin to manipulate users by adding, updating, or removing ore effectively
* **Extract data**: provide an option for user to download items list, users list, example: download as an Excel file
## 4. Project Functions/Features
### Product manipulate
* **Insert/Add**: to add a new product to the storage by input its information
* **Update**: to update/change current infor of a product
* **Delete**: to delete/remove a product from the storage
* **Search**: to search/filter/find any item by the given input data
* **Diplay**: display the current products and their information in table
### User and account
* **Log-in**: by inputing username and its corespoding password/code
* **Log-out**: logged out of the current user and leave the main page to the log-ing page
* **Sign-Up**: register a new user
* **Change password**: allowed a user to change their account's password
### Other features
* **Mode switch**: switch between dark and light mode
* **Note box**: to guide users on how to use the app properly
* **Message box**: to feedback on user action
## 5. Expected number of pages
### Current available pages (4):
* **Log-in page**: landing page
* **Sign-in page**: to register new user
* **Change password** page
* **Main page**: for managing product inventory
### Upcoming pages:
* **Activity log page**: show all the changes/history
* **User manager page**: for admin uses to manage users (add, delete, update)
* **Extract data page**: for user to select items in the storage and download
* **Sell-driven inventory update page**: for real-time update an item's data in the stock triggered by a sale
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
# Intruction on how to use the application
## 1. Run the **sql_command.py** file

  
  


