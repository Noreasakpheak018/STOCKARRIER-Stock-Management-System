import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import mysql.connector
from decimal import Decimal
from dateutil.relativedelta import relativedelta
from sql_command import db_host, db_username, db_password

user_list = ["Username","Admin"]
category_lst = ["NULL","Soft-drink", "Milk", "Ingredient", "Chips", "Burger", "Source", "Oil"]
status_lst = ["Available", "Out Of Stock", "On Ordering","Expired"]
partner_companies_list = ["NULL","CocaCola", "BeverageKing", "DrinkCampanyKH", "SnackCompanyKH", "HomeCooker",
                        "BurgerGod", "GodsIngredient"]
column_list = ["ID","Name","Price", "Quantity", "Unit", "Category", "Import",
             "Expire", "ShelfLife","Supplier", "Status"]
unit_list = ["NULL", "200mL can", "500mL bottle", "1L bottle", "200g piece","0.5kg piece", "1kg piece", "100g bag", "200g bag"]
search_type = {"ID":(0, 'int'),"ProductName":(1, 'str'), "PricePerUnit":(2, 'int)'), "Quantity":(3, 'int'),
             "Category":(5, 'str'), "Supplier":(8, 'str'), "Status":(9, 'str')}
current_user = ""
today = datetime.date.today()
import_lst = ["yyyy-mm-dd", "Today"]
days = [day for day in range(1, 32)]
months = [month for month in range(1, 13)]
years = [year for year in range(2024, 2051)]
largest_id = 0
item_couter = 0



def load_data():
    erase_table()
    reset_element()
    for col_name in column_list:
        treeview.heading(col_name, text= col_name)

    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()

    cs.execute("SELECT * FROM ProductStorage;")
    data_list = cs.fetchall()

    for data in data_list:
        treeview.insert('', tk.END, values= data)
        print(data)
    
    cs.execute("SELECT MAX(ID) FROM ProductStorage;")
    global largest_id
    global item_couter
    largest_id = cs.fetchone()[0] 
    item_couter = len(data_list)

    cs.close()
    database.close()

    row_counter(count_all=True)
    print("Loaded data from Product table")

def login():
    username = user_cb.get()
    password = passw_ent.get()

    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()

    query = f"SELECT Passcode, UserRole FROM UserTable WHERE UserName = '{username}';"
    try:
        cs.execute(query)
        result = cs.fetchall()
        passcode =result[0][0]
        role = result[0][1]

        print("Valid password: ", passcode)
    except:
        message_update("Invalid Username", login_mes=True)
        print("Invalid Username")
        return
    
    if password == passcode:
        global current_user 
        current_user = username
        main_user_lb.config(text= f"Logged in as: {current_user} ({role})")
        print(f"current user {current_user}")
        disable_frame(login_frame)
        enable_frame(main_frame, treeFrame)
        showVar.set(True)
        load_data()
        message_update("Logged In")
        print("Logged in")
    else:
        message_update("Invalid Password", login_mes=True)
        print("Invalid Password")

def reset_pass_checker():
    username = user_fg_entry.get()
    phone = phone_fg_entry.get()
    email = email_fg_entry.get()
    birth = db_fg_entry.get()

    check = [username, phone, email, birth]
    for i in check:
        if i:
            if i in ["Username", "Phone Number", "Email", "Date of Birth"]:
                instr_label.config(text="Invalid User infor")
                print("Invalid User infor")
                return
        else:
            instr_label.config(text="Please input user infor")
            print("Empty")
            return
    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()
    query = f"SELECT * FROM UserTable WHERE UserName = '{username}';"
    try:
        cs.execute(query)
        result = cs.fetchall()[0]
        print(result)
        print(str(result[4]) == birth)
        if result:
            if result[1] == username and result[2] == phone and result[3] == email and str(result[4]) == birth:
                instr_label.config(text="Input new password")
                disable_widget(user_fg_entry, phone_fg_entry, email_fg_entry, db_fg_entry, reset_button)
                enable_widget(new_pass_label, new_pass_label2, set_pass)
            else:
                instr_label.config(text="Invalid User infor")
    except:
        print("Invalid username")
        instr_label.config(text="Invalid username")
        
    cs.close()
    database.close()
    return username
     
def reset_password():
    username = reset_pass_checker()
    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()
    
    pass1 = new_pass_label.get()
    pass2 = new_pass_label2.get()
    
    for i in [pass1, pass2]:
        if i in ["New password", "Input the same password"]:
            instr_label.config(text="Please input password")
            return
        else:
            if not i:
                instr_label.config(text="Please input password")
                return
    if pass1 == pass2:
        query = f"UPDATE UserTable SET Passcode = '{pass1}' WHERE UserName = '{username}';"
        cs.execute(query)
        database.commit()
        instr_label.config(text="Password reset successfully")
    else:
        instr_label.config(text="Passwords do not match")
    cs.close()
    database.close()

def signup():
    print("12")
    username = user_su_entry.get()
    phone = phone_su_entry.get()
    email = email_su_entry.get()
    birth = db_su_entry.get()
    pw1 = su_pass_label.get()
    pw2 = su_pass_label2.get()
    
    if pw1 != pw2:
        print("Please input matched passwords")
        instr_label2.config(text="Please matched passwords")
        return 

    check = [username, phone, email, birth]
    for i in check:
        if i:
            if i in ["Username", "Phone Number", "Email", "Date of Birth"]:
                instr_label2.config(text="Invalid User infor")
                print("Invalid User infor")
                return
        else:
            instr_label2.config(text="Please input user infor")
            print("Empty")
            return
        
    
    
    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()
    

    query = f"""
        INSERT INTO UserTable (UserName, Phone, Email, BirthDate, Passcode, UserRole, UserStatus)
        VALUES ('{username}', '{phone}', '{email}', '{birth}', '{pw1}', 'employee', 'Active');
        """
    cs.execute(query)
    try:
        
        database.commit()
        print("User added successfully")
        instr_label2.config(text="User added successfully")
    except:
        print("Failed to add user")
        instr_label2.config(text="Failed to add user")
    
    print(24)
    cs.close()
    database.close()

def logout():
    disable_frame(main_frame, treeFrame)
    enable_frame(login_frame)
    showVar.set(False)
    show_ps.set(False)
    show_pass()
    user_cb.set(user_list[0])
    passw_ent.delete(0, "end")
    passw_ent.insert(0, "Password")

    print(f"Logged Out: {current_user}")

def insert_row():
    if not input_verify():
        return
    val = get_input("all")

    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()
    global largest_id
    largest_id += 1
    val[0] = largest_id
    query = f"""INSERT INTO ProductStorage (ID, ProductName, PricePerUnit, Quantity, Unit, Category,
                                             Import_Date, Expire_Date, Shelf_Life, Supplier, Status)
                                    VALUES ({val[0]}, '{val[1]}', {float(val[2])}, {int(val[3])}, '{val[4]}','{val[5]}',
                                             '{val[6]}','{val[7]}','{val[8]}', '{val[9]}', '{val[10]}');
                                """

    cs.execute(query)
    database.commit()

    cs.close()
    database.close()
    
    
   

    insert_table(val)
    global item_couter 
    row_counter(num=item_couter+1)
    reset_element()

    message_update("Insert Succeed")
    print("Insert Succeed")

def delete_row():
    
    pro_id = filter_entry.get()
    
    if not pro_id:
        message_update("Please search the item first")
        return
    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )

    cs = database.cursor()

    query = f"DELETE FROM ProductStorage WHERE ID = {pro_id};"

    messssage = messagebox.askyesno(f"Delete item ID {pro_id}", "Are you sure to delete this item?")
    if messssage:
        try:
            cs.execute(query)
            database.commit()

            cs.close()
            database.close()

            erase_table()
            insert_table(["Deleted" for i in range(11)])
            row_counter(num=0)
            message_update(f"Deleted item ID:{pro_id}")
            row_counter()
            reset_element()
            print(f"Deleted item ID:{pro_id}")
        except:
            message_update(f"Unable to delete item ID:{pro_id}")
            print(f"Unable to delete item ID:{pro_id}")
    else:
        message_update(f"Delete cancelled")
        print(f"Delete cancelled")
    
def update_row():

    val = get_input("all")
    if not val:
        return

    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()

    try:
        query = f"""UPDATE ProductStorage
                    SET ProductName = '{val[1]}',   PricePerUnit = {float(val[2])},  Quantity = {int(val[3])},
                        Category = '{val[4]}', Unit = '{val[5]}', Import_Date = '{val[6]}', 
                        Expire_Date = '{val[7]}', Shelf_Life = '{val[8]}', Supplier = '{val[9]}', Status = '{val[10]}'
                    WHERE ID = {val[0]};"""
        cs.execute(query)
        database.commit()

        erase_table()
        insert_table(val)
        message_update(f"Updated item ID: {val[0]}")
        print(f"Updated item ID: {val[0]}")
    except:
        message_update(f"Something's wrong! Unable to update item ID: {val[0]}")
        print("Something's wrong")
    
    cs.close()
    database.close()

def search_row():
    type_ = filter_combobox.get()
    value = filter_entry.get()

    if not value:
        message_update("Empty Search")
        print("Empty search")
        return

    print(f"Search for {type_}:{value}")
    

    database = mysql.connector.connect(
        host = db_host,
        user = db_username,
        password = db_password,
        database = "Stock_Management"
    )
    cs = database.cursor()
    if not any(i in "!@#$%^&*?/|\\," for i in value):
        if value.isalpha() or any(i in " -" for i in value):
            query = f"""SELECT * FROM ProductStorage 
                        WHERE  LOWER(REGEXP_REPLACE({type_}, '[ -]', '')) = LOWER(REGEXP_REPLACE('{value}', '[ -]', ''));"""
        elif is_number(value):
            query = f"SELECT * FROM ProductStorage WHERE {type_} = {value};"
        else:
            query = f"SELECT * FROM ProductStorage WHERE {type_} {value};"

        try:
            cs.execute(query)
            result = cs.fetchall()
            print("Search result:", result)

            erase_table()
            row_counter()

            if result:
                for row in result:
                    insert_table(row)
                
                id_entry.config(state='normal')
                id_entry.delete(0, tk.END)
                id_entry.insert(0, result[0][0])
                id_entry.config(state='disable')

                set_input(result[0])
                row_counter(num= len(result))
                message_update("Search found")
                print("Search found")
            else:
                message_update("Not found")
                print("Not found")
        except:
            message_update("Something's Wrong!")
            print("Something's wrong in searching")
    else:
        message_update("Invalid Input")
        print("Invalid input")

    cs.close()
    database.close()



def row_counter(count_all = False, num = 0):
    if count_all:
        global item_couter
        total_item_label.config(text=f"Total: {item_couter} items")
    else:
        total_item_label.config(text=f"Total: {num} items")

def erase_table(all = True, id= None):
    try:
        if all:
            for item in treeview.get_children():
                treeview.delete(item)
        else:
            treeview.delete(id)
    except:
        print("Empty table")

def insert_table(val_list):
    treeview.insert('', tk.END, values= val_list)

def input_verify():
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    try:
        float(price)
        int(quantity)
    except:
        message_update("Invalid input: wrong input type of Price or Quantity")
        print("Invalid input: wrong input type of Price or Quantity")
        return False

    for i in [name, price, quantity]:
        if not i:
            message_update("Empty Input")
            print("Empty input")
            return False
        if i in ["Product Name", "Price per unit", "Quantity"]:
            message_update("Invalid: please input proper Name, Price or Quantity")
            print("Invalid: not input")
            return False

    return True

def get_input(*args):
    pro_id = id_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    unit = unit_combobox.get()
    category = category_combobox.get()
    unit = unit_combobox.get()
    supplier = supplier_cb.get()
    status = status_combobox.get()

    import_date = import_combobox.get()

    if import_date.lower() in ['today', 'yyyy-mm-dd']:
        import_date = today
    else:
        try:
            parts = import_date.split('-')
            y = int(parts[0])
            m = int(parts[1])
            d = int(parts[2])
            import_date = datetime.date(y, m, d)
        except:
            message_update("Error import date")
            print("Error import date")
            return []

    year = int(year_spinbox.get())
    month = int(month_spinbox.get())
    day = int(day_spinbox.get())

    exp = datetime.date(year, month, day)

    shelf_life = relativedelta(exp, import_date)
    shelf_life = f"{shelf_life.years}y-{shelf_life.months}m-{shelf_life.days}d"


    val_list = [pro_id, name, price, quantity, unit, category, import_date, exp, shelf_life, supplier, status]
    return_list = []
    
    if args[0] == 'all':
        return val_list

    for type_, column in zip(args, column_list):
        if type_.lower() == column.lower():
            return_list.append(val_list[column_list.index(column)])
    return return_list
    
def set_input(val_list):
    print(val_list)
    print(val_list[2], val_list[7].year, val_list[7].month,val_list[7].day)
    id_entry.config(state="normal")
    id_entry.delete(0, "end")
    id_entry.insert(0, val_list[0])
    id_entry.config(state="disable")

    name_entry.delete(0, "end")
    name_entry.insert(0, val_list[1])
    price_entry.delete(0, "end")
    price_entry.insert(0, val_list[2])
    quantity_entry.delete(0, "end")
    quantity_entry.insert(0, val_list[3])

    unit_combobox.set(f"{val_list[4]}")
    category_combobox.set(f"{val_list[5]}")
    import_combobox.set(f"{val_list[6]}")
    
    year_spinbox.set(val_list[7].year)
    month_spinbox.set(val_list[7].month)
    day_spinbox.set(val_list[7].day)

    supplier_cb.set(f"{val_list[9]}")
    status_combobox.set(f"{val_list[10]}")
    


def message_update(txt, login_mes=False):
    if login_mes:
        message_l.config(text=txt)
    else:
        message_label.config(text=txt)

def is_number(num):
    try:
        float(num)
        return True
    except:
        return False

def toggle_mode():
    dark_color = "#303030"
    if dark_mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
        dark_mode_switch.config(text="Light Mode")
        root.config(background="white")

    else:
        style.theme_use("forest-dark")
        dark_mode_switch.config(text="Dark Mode")
        root.config(background= dark_color)

def switch_state():
    if id_switch_val.get():
        id_entry.config(state="normal")
        id_switch.config(text="Enabled ID input")
        
    else:
        id_entry.config(state="disable")
        id_switch.config(text="Disabled ID input")

def show_pass():
    if show_ps.get():
        passw_ent.config(show="")
    else: 
        passw_ent.config(show="*")

def reset_element():
    global largest_id

    id_entry.config(state="normal")
    id_entry.delete(0, "end")
    id_entry.insert(0, largest_id+1)
    id_entry.config(state="disable")

    name_entry.delete(0, "end")
    name_entry.insert(0, "Product Name")
    price_entry.delete(0, "end")
    price_entry.insert(0, "Price Per Unit")
    quantity_entry.delete(0, "end")
    quantity_entry.insert(0, "Quantity")

    category_combobox.set(category_lst[0])
    import_combobox.set(import_lst[0])
    status_combobox.set(status_lst[0])
    unit_combobox.set(unit_list[0])
    supplier_cb.set(partner_companies_list[0])

    year_spinbox.set(years[1])
    month_spinbox.set(months[0])
    day_spinbox.set(days[0])

    filter_entry.delete(0, 'end')



def enable_frame(*args):
    for frame in args:
        frame.grid()
    
def disable_frame(*args):
    for frame in args:
        frame.grid_remove()

def disable_widget(*args):
    for widget in args:
        widget.pack_forget()

def enable_widget(*args):
    for widget in args:
        widget.pack(side = "top", pady=10, padx=10)





if __name__ == "__main__":
    #root
    root = tk.Tk()

    root.title("Stock Manager")
    style = ttk.Style(root)
    root.tk.call("source", "forest-light.tcl")
    root.tk.call("source", "forest-dark.tcl")
    style.theme_use("forest-dark")
    root.geometry("1500x650")
    root.resizable(False, False)



    #login frame
    login_frame = ttk.Frame(root)
    login_frame.grid(row=0, column=0)
    login_frame.grid_propagate(False)

    app_name_font = font.Font(family="Arial", size= 30, weight="bold")
    app_name_l = ttk.Label(login_frame, text="Stock Manager", font= app_name_font)
    app_name_l.pack(side= "top", pady=30, padx= 30)

    #login system message
    message_l = ttk.Label(login_frame, text="Login to use the system.")
    message_l.pack(side='top')

    #user photo / image
    user_icon = ImageTk.PhotoImage(Image.open('user_icon.png').resize((100, 100)))
    icon_l = ttk.Label(login_frame, image= user_icon)
    icon_l.pack(side= "top", pady= 30)


    #account label
    account_lf = ttk.LabelFrame(login_frame, text="Acount")
    account_lf.pack(side= 'top', padx=10, pady= (0, 10))

    #usernama combobox
    user_cb = ttk.Combobox(account_lf, values= user_list, width= 30)
    user_cb.current(0)
    user_cb.grid(row=0, column=0, padx=10, pady=10, sticky='we')

    #password entry
    passw_ent = ttk.Entry(account_lf, width= 30, show="*")
    passw_ent.insert(0, "Password")
    passw_ent.bind("<FocusIn>", lambda x: passw_ent.delete('0', 'end'))
    passw_ent.grid(row=1, column=0, padx=10, sticky="we")

    #show password checkbox
    show_ps = tk.BooleanVar()
    show_ps_chb = ttk.Checkbutton(account_lf, text="Show password", variable=show_ps, command= show_pass)
    show_ps_chb.grid(row=3, column=0, padx=10, pady=10, sticky= 'w')

    #login button
    login_button = ttk.Button(account_lf, text=	"Login", command= login)
    login_button.grid(row=4, column=0, padx=5, pady=10, sticky= 'we')

    #forget password button
    forget_ps_button = ttk.Button(account_lf, text=	"Forget Password", command=lambda: [disable_frame(login_frame), enable_frame(forget_password_frame)])
    forget_ps_button.grid(row=5, column=0, padx=5, pady=5, sticky= 'we')

    #sign up button
    signup_button = ttk.Button(account_lf, text=	"Sign up", command=lambda: [disable_frame(login_frame), enable_frame(signup_frame)])
    signup_button.grid(row=6, column=0, padx=5, pady=5, sticky= 'we')




    #sign up frame
    signup_frame = tk.Frame(root)
    signup_frame.grid(row=0, column=0)

    app_name_ls = ttk.Label(signup_frame, text="Stock Manager", font= app_name_font)
    app_name_ls.pack(side= "top", pady=30, padx= 30)

    signup_lb = ttk.LabelFrame(signup_frame, text="Sign Up")
    signup_lb.pack(padx=10, pady=10, side= 'top')

    #instructor label2
    instr_label2 = ttk.Label(signup_lb, text="Input infor below to signup", width=30)
    instr_label2.pack(side='top', padx=10, pady=10)

    #new username entry
    user_su_entry = ttk.Entry(signup_lb, width= 30)
    user_su_entry.insert(0, "Username")
    user_su_entry.bind("<FocusIn>", lambda x: user_su_entry.delete('0', 'end'))
    user_su_entry.pack(side = "top", padx=10, pady=10)

    #new phone entry
    phone_su_entry = ttk.Entry(signup_lb, width= 30)
    phone_su_entry.insert(0, "Phone Number")
    phone_su_entry.bind("<FocusIn>", lambda x: phone_su_entry.delete('0', 'end'))
    phone_su_entry.pack(side = "top", padx=10, pady=10)

    #email entry
    email_su_entry = ttk.Entry(signup_lb, width= 30)
    email_su_entry.insert(0, "Email")
    email_su_entry.bind("<FocusIn>", lambda x: email_su_entry.delete('0', 'end'))
    email_su_entry.pack(side = "top", padx=10, pady=10)

    #date of birth entry
    db_su_entry = ttk.Entry(signup_lb, width= 30)
    db_su_entry.insert(0, "Date of Birth: yyyy-mm-dd")
    db_su_entry.bind("<FocusIn>", lambda x: db_su_entry.delete('0', 'end'))
    db_su_entry.pack(side = "top", padx=10, pady=10)

    #new password entries
    su_pass_label = ttk.Entry(signup_lb, width=30)
    su_pass_label.insert(0, "New Password")
    su_pass_label.bind("<FocusIn>", lambda x: su_pass_label.delete('0', 'end'))
    su_pass_label.pack(side = "top", pady=10, padx=10)

    su_pass_label2 = ttk.Entry(signup_lb, width=30)
    su_pass_label2.insert(0, "Input the same password")
    su_pass_label2.bind("<FocusIn>", lambda x: su_pass_label2.delete('0', 'end'))
    su_pass_label2.pack(side = "top", pady=10, padx=10)

    #signup button
    sign_button = ttk.Button(signup_lb, text="Sign Up", command= signup)
    sign_button.pack(side = "top", padx=10, pady=10)

    back_button = ttk.Button(signup_lb, text="Back", command=lambda: [disable_frame(signup_frame), enable_frame(login_frame)])
    back_button.pack(side= "bottom", pady=(5, 10))




    #forget password frame
    forget_password_frame = ttk.Frame(root)
    forget_password_frame.grid(row=0, column=0)

    app_name_lo = ttk.Label(forget_password_frame, text="Stock Manager", font= app_name_font)
    app_name_lo.pack(side= "top", pady=30, padx= 30)



    #reset password labelframe
    reset_pass_lb = ttk.LabelFrame(forget_password_frame, text="Reset Password")
    reset_pass_lb.pack(padx=10, pady=10, side= 'top')

    #instructor label
    instr_label = ttk.Label(reset_pass_lb, text="Input infor below to reset password", width=30)
    instr_label.pack(side='top', padx=10, pady=10)

    #username entry
    user_fg_entry = ttk.Entry(reset_pass_lb, width= 30)
    user_fg_entry.insert(0, "Username")
    user_fg_entry.bind("<FocusIn>", lambda x: user_fg_entry.delete('0', 'end'))
    user_fg_entry.pack(side = "top", padx=10, pady=10)

    #phone entry
    phone_fg_entry = ttk.Entry(reset_pass_lb, width= 30)
    phone_fg_entry.insert(0, "Phone Number")
    phone_fg_entry.bind("<FocusIn>", lambda x: phone_fg_entry.delete('0', 'end'))
    phone_fg_entry.pack(side = "top", padx=10, pady=10)

    #email entry
    email_fg_entry = ttk.Entry(reset_pass_lb, width= 30)
    email_fg_entry.insert(0, "Email")
    email_fg_entry.bind("<FocusIn>", lambda x: email_fg_entry.delete('0', 'end'))
    email_fg_entry.pack(side = "top", padx=10, pady=10)

    #date of birth entry
    db_fg_entry = ttk.Entry(reset_pass_lb, width= 30)
    db_fg_entry.insert(0, "Date of Birth")
    db_fg_entry.bind("<FocusIn>", lambda x: db_fg_entry.delete('0', 'end'))
    db_fg_entry.pack(side = "top", padx=10, pady=10)

    #reset password button
    reset_button = ttk.Button(reset_pass_lb, text="Reset", command= reset_pass_checker)
    reset_button.pack(side = "top", padx=10, pady=10)

    #new password entries
    new_pass_label = ttk.Entry(reset_pass_lb, width=30)
    new_pass_label.insert(0, "New Password")
    new_pass_label.bind("<FocusIn>", lambda x: new_pass_label.delete('0', 'end'))
    new_pass_label.pack(side = "top", pady=10, padx=10)

    new_pass_label2 = ttk.Entry(reset_pass_lb, width=30)
    new_pass_label2.bind("<FocusIn>", lambda x: new_pass_label2.delete('0', 'end'))
    new_pass_label2.insert(0, "Input the same password")
    new_pass_label2.pack(side = "top", pady=10, padx=10)

    #set new password button
    set_pass = ttk.Button(reset_pass_lb, text="Set password", command = reset_password)
    set_pass.pack(side="top")




    #home / back button
    home_button = ttk.Button(reset_pass_lb, text="Back", command=lambda: [disable_frame(forget_password_frame), enable_frame(login_frame)])
    home_button.pack(side= "bottom", pady=(5, 10))

    disable_widget(new_pass_label, new_pass_label2, set_pass)




    #main frame
    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, sticky= "n")



    #current user label / display
    main_acount_lf = ttk.LabelFrame(main_frame, text="Account")
    main_acount_lf.grid(row=0, column=0, padx=10, pady=10, sticky= "we")

    main_user_lb = ttk.Label(main_acount_lf,text= "")
    main_user_lb.pack(side= "left", pady= (0, 10), padx= 10)

    #log out button
    logout_bt = ttk.Button(main_acount_lf, text="Log out", command= logout)
    logout_bt.pack(side='right', pady= (0, 10), padx= 10)



    # Seperator line 1
    Seperator1 = ttk.Separator(main_frame)
    Seperator1.grid(row=1, column=0, padx=5, pady=5, sticky="we")



    #widget label frame
    widgets_frame = ttk.LabelFrame(main_frame, text="Product Information")
    widgets_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    #id label
    id_label = ttk.Label(widgets_frame, text="ID")
    id_label.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="e")

    id_entry = ttk.Entry(widgets_frame)
    id_entry.insert(0, largest_id)
    id_entry.bind("<FocusIn>", lambda e: id_entry.delete('0', 'end'))
    id_entry.grid(row=0, column=1, padx=5, pady=(0, 5) , sticky="ew")
    id_entry.config(state="disable")

    #name label
    name_label = ttk.Label(widgets_frame, text="Name")
    name_label.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="e")

    name_entry = ttk.Entry(widgets_frame)
    name_entry.insert(0, "Product Name")
    name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
    name_entry.grid(row=1, column=1, padx=5, pady=(0, 5), sticky="ew")

    #price label
    price_label = ttk.Label(widgets_frame, text="Price")
    price_label.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="e")

    price_entry = ttk.Entry(widgets_frame)
    price_entry.insert(0, "Price per unit")
    price_entry.bind("<FocusIn>", lambda e: price_entry.delete('0', 'end'))
    price_entry.grid(row=2, column=1, padx=5, pady=(0, 5), sticky="we")

    #quantity label
    quantity_label = ttk.Label(widgets_frame, text="QTY")
    quantity_label.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="e")

    quantity_entry = ttk.Entry(widgets_frame)
    quantity_entry.insert(0, "Quantity")
    quantity_entry.bind("<FocusIn>", lambda e: quantity_entry.delete('0', 'end'))
    quantity_entry.grid(row=3, column=1, padx=5, pady=(0, 5), sticky="ew")


    #unit label
    unit_label = ttk.Label(widgets_frame, text="Unit")
    unit_label.grid(row=4, column=0, padx=5, pady=(0, 5), sticky="e")

    unit_combobox = ttk.Combobox(widgets_frame, values=unit_list)
    unit_combobox.current(0)
    unit_combobox.grid(row=4, column=1, padx=5, pady=(0, 5), sticky="ew")


    #category label
    category_label = ttk.Label(widgets_frame, text="CTG")
    category_label.grid(row=0, column=2, padx=5, pady=(0, 5), sticky="e")

    category_combobox = ttk.Combobox(widgets_frame, values=category_lst)
    category_combobox.current(0)
    category_combobox.grid(row=0, column=3, padx=5, pady=(0, 5), sticky="ew")

    #status label
    status_label = ttk.Label(widgets_frame, text="Status")
    status_label.grid(row=1, column=2, padx=5, pady=(0, 5), sticky="e")

    status_combobox = ttk.Combobox(widgets_frame, values=status_lst)
    status_combobox.current(0)
    status_combobox.grid(row=1, column=3, padx=5, pady=(0, 5), sticky="ew")

    #supplier label
    supplier_lb = ttk.Label(widgets_frame, text="Supplier")
    supplier_lb.grid(row=2, column=2, padx=5, pady=(0, 5), sticky="e")

    supplier_cb = ttk.Combobox(widgets_frame, values=partner_companies_list)
    supplier_cb.current(0)
    supplier_cb.grid(row=2, column=3, padx=5, pady=(0, 5), sticky="ew")

    #import date
    import_label = ttk.Label(widgets_frame, text="Import")
    import_label.grid(row=3, column=2, padx=5, pady=(0, 5), sticky="e")

    import_combobox = ttk.Combobox(widgets_frame, values=import_lst)
    import_combobox.current(0)
    import_combobox.grid(row=3, column=3, padx=5, pady=10, sticky="ew")

    #expire label
    exp_label = ttk.Label(widgets_frame, text="EXP:")
    exp_label.grid(row=4, column=2, padx=5, pady=(0, 5), sticky="e")

    exp_label2 = ttk.Label(widgets_frame)
    exp_label2.grid(row=4, column=3, padx=5, pady=(0, 5), sticky="e")

    #expire day
    day_l = ttk.Label(exp_label2, text="d")
    day_l.grid(row=0, column=0)

    day_spinbox = ttk.Combobox(exp_label2, values=days, width=2)
    day_spinbox.insert(0, days[0])
    day_spinbox.grid(row=0, column=1, padx=(1, 5))

    #expire month
    month_l = ttk.Label(exp_label2, text="m")
    month_l.grid(row=0, column=2)

    month_spinbox = ttk.Combobox(exp_label2, values=months, width=2)
    month_spinbox.insert(0, months[0])
    month_spinbox.grid(row=0, column=3, padx=(1, 5))

    #expire year
    year_l = ttk.Label(exp_label2, text="y")
    year_l.grid(row=0, column=4)

    year_spinbox = ttk.Combobox(exp_label2, values=years, width=4)
    year_spinbox.insert(0, years[1])
    year_spinbox.grid(row=0, column=5, padx=(1, 5))



    #interaction / interactor frame
    interaction_frame = ttk.LabelFrame(main_frame, text= "Interactor")
    interaction_frame.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")

    #insert button
    insert_button = ttk.Button(interaction_frame, text= "Insert", command= insert_row)
    insert_button.grid(row=0, column=0, padx=5, pady=5)

    #update button
    update_button = ttk.Button(interaction_frame, text= "Update", command=update_row)
    update_button.grid(row=0, column=1, padx=5, pady=5)

    #delete button
    delete_button = ttk.Button(interaction_frame, text= "Delete", command= delete_row)
    delete_button.grid(row=0, column=2, padx=5, pady=5)

    #display all button
    display_all_button = ttk.Button(interaction_frame, text= "Display all", command=load_data)
    display_all_button.grid(row=0, column=3, padx=5, pady=5)

    #show table checkbox
    showVar = tk.BooleanVar()
    show_table_chb = ttk.Checkbutton(interaction_frame, text="Show table", variable=showVar, command=lambda: treeFrame.grid() if showVar.get() else treeFrame.grid_remove())
    show_table_chb.grid(row=0, column=4, padx=5, pady=5)



    #filter / search frame
    filter_frame = ttk.LabelFrame(main_frame, text= "Filter")
    filter_frame.grid(row=4, column=0, padx=10, pady=(0,5), sticky="we")

    #search type
    filter_label = ttk.Label(filter_frame, text="By: ")
    filter_label.grid(row=0, column=0, padx=5, pady=5)

    filter_combobox = ttk.Combobox(filter_frame, width= 15, state= "readonly", values= list(search_type.keys()))
    filter_combobox.current(0)
    filter_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    #search / filter entry
    filter_label2 = ttk.Label(filter_frame, text="Enter: ")
    filter_label2.grid(row=0, column=2, padx=5, pady=5, sticky="e")

    filter_entry = ttk.Entry(filter_frame)
    filter_entry.bind("<FocusIn>", lambda e: filter_entry.delete('0', 'end'))
    filter_entry.grid(row=0, column=3, padx=5, pady=5)

    #search button
    search_button = ttk.Button(filter_frame, text="Search", command= search_row)
    search_button.grid(row=0, column=4, padx=5, pady=10)



    # Seperator2
    Seperator2 = ttk.Separator(main_frame)
    Seperator2.grid(row=5, column=0, padx=5, pady=5, sticky="we")



    # note frame
    note_frame = ttk.LabelFrame(main_frame, text="Notes")
    note_frame.grid(row=6, column=0, padx=10, pady=5,sticky="we")

    note_txt = "{}\n{}\n{}".format(
        "Insert-Button autometically add new item to the end of the list with largest ID.",
        "Update and Delete-Button works after using Search-Button.",
        "Only Admin can user Delete-Button."
    )

    #note label             
    note_label = ttk.Label(note_frame, text=note_txt)
    note_label.grid(row=0, column=0, padx=10, pady=10,sticky="we")


    #setting frame
    footer_frame = ttk.LabelFrame(main_frame, text="Setting")
    footer_frame.grid(row=7, column=0, padx=10, pady=5, sticky="news")

    #dark mode
    dark_mode_switch = ttk.Checkbutton(footer_frame, text="Dark Mode", style="Switch", command= toggle_mode)
    dark_mode_switch.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    #switch id-input state
    id_switch_val = tk.IntVar()
    id_switch = ttk.Checkbutton(footer_frame, text= "ID state", variable= id_switch_val, onvalue=1, offvalue=0, style="Switch", command= switch_state)
    id_switch.grid(row=0, column=1, padx=10, pady=5, sticky="w")


    # the frame on the right side / table frame
    treeFrame = ttk.Frame(root)
    treeFrame.grid(row=0, column=1, padx=(5, 20), sticky="n")



    # notification labelframe / system message
    message_frame = ttk.LabelFrame(treeFrame, text="System Message")
    message_frame.pack(side="top", expand= True, fill='both', pady=(10, 20))

    message_label = ttk.Label(message_frame, text="", wraplength="750", justify= "left")
    message_label.pack(fill="both", expand=True, pady=12, padx=10)


    #scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    #table
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=column_list, height=15)
    treeview.pack(side='top')

    #customize widget for each row
    treeview.column("ID", width=30, stretch=False)
    treeview.column("Name", width=125, stretch=False)
    treeview.column("Price", width=50, stretch=False)
    treeview.column("Quantity", width=50, stretch=False)
    treeview.column("Unit", width=75, stretch=False)
    treeview.column("Category", width=100, stretch=False)
    treeview.column("Import", width=75, stretch=False)
    treeview.column("Expire", width=75, stretch=False)
    treeview.column("ShelfLife", width=75, stretch=False)
    treeview.column("Supplier", width=120, stretch=False)
    treeview.column("Status", width=100, stretch=False)

    treeScroll.config(command=treeview.yview)

    #row number to display
    row_idi_frame = ttk.LabelFrame(treeFrame, text="Row display")
    row_idi_frame.pack(side="right") 

    row_spinbox = ttk.Spinbox(row_idi_frame, from_= 10, to=21, command= lambda:  treeview.config(height= row_spinbox.get()))
    row_spinbox.insert(0, 20)
    row_spinbox.pack(padx=5, pady=5)

    #total item on table counter
    total_item_frame = ttk.LabelFrame(treeFrame, text="Item counter")
    total_item_frame.pack(side="left") 

    total_item_label = ttk.Label(total_item_frame, text="")
    total_item_label.pack(padx=10, pady=10)



    disable_frame(main_frame, treeFrame, forget_password_frame, signup_frame)



    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
