import sqlite3
import pandas as pd
import re
def login():
    username = input(" Enter Email ID : ")
    if not re.match("[a-zA-Z0-9]\S*@\S*[a-zA-Z]", username):
        print("ERROR..!!! Not a Valid Email-id")
        username = input("enter a valid Email ID:") 
    print(username)
    password = input(" Enter Password : ")
    curs=conn.cursor()
    curs.execute(" select cust_id from customer_master where email_id =? and password =?",(username,password))
    lst = curs.fetchall()
    for tup in lst:
        for element in tup:
            cust_id = str(element)
            #print(cust_id)
    login=open('login.txt','w')
    if(len(lst)>0):
        print("Succefull")
        
        login.write(cust_id)
    else:
        print("Email ID/Password Incorrect")
        print("Login Denied")
    login.close()
def show_menu():
	print(pd.read_sql_query("select * from shop_menu", conn))
	
def new_user():
        print("======| Please enter the Customer Details |======")
        cust_fname = input(" First Name(only 15 characters) : ")
        while (len(cust_fname)>15) or not re.match("^[a-zA-z]*$",cust_fname):
            print("Error! Only 15 characters a-z allowed.")
            cust_fname = input(" First Name : ")
            
        cust_lname = input(" Last Name(only 15 characters) : ")
        while (len(cust_lname)>15) or not re.match("^[a-zA-z]*$",cust_lname):
            print("Error! Only 15 characters a-z allowed.")
            cust_lname = input(" Last Name : ")
        cust_address = input(" Address : ")
        cust_pincode = input(" Pincode(maximum 10 characters : ")
        while (len(cust_pincode)>10) or not re.match("^[0-9]*$",cust_pincode):
            print("Error! Only 10 digits allowed")
            cust_pincode = int(input(" Pincode : "))
        cust_mobileno = input(" Mobile Number(10 digits) : ")
    
        while (len(cust_mobileno)!=10):
            print("Error! Only 10 digits 0-9 allowed.")
            cust_mobileno = input(" Mobie Number :")
        email_id = input(" Email ID : ")
        if not re.match("[a-zA-Z0-9]\S*@\S*[a-zA-Z]", email_id):
            print("ERROR..!!! Not a Valid Email-id")
            email_id = input("enter a valid Email ID:") 
        cust_password = input(" Password :")
        curs = conn.cursor()
        curs.execute("INSERT INTO customer_master (cust_fname, cust_lname, cust_address, cust_pincode, mobileno,email_id,password) values (?,?,?,?,?,?,?)",
                     (cust_fname, cust_lname, cust_address, cust_pincode, cust_mobileno,email_id,cust_password))
        print("======| NEW CUSTOMER ADDED SUCCESSFULLY |======\n")
        conn.commit()
def info():
    print("WE ARE AWESOME !!")
	
													
		




## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
	print('=================================\n')
	print('  WELCOME TO HII HUNGRY  \n')
	print('=================================\n')
	print(' Please choose from the following option : ')
	print()
	print('1. NEW USER \n')
	print('2. LOGIN \n')
	print('3. SHOW MENU \n')
	print('4. ABOUT US \n')
	print()
	print('0. To EXIT the program \n')

	choice =input("Please Enter Your Option : ")
	if choice == '1':
		new_user()
	elif choice == '2':
		login()
	elif choice == '3':
		show_menu()
	elif choice == '4':
		info()
	elif choice == '0':
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")
		print("Please enter a valid option")
