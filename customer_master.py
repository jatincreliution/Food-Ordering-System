import sqlite3
import re
import pandas as pd
def add_rec():
        print("======| Please enter the Customer Details |======")
        
        cust_fname = input(" First Name(only 15 characters): ")
        while (len(cust_fname)>15) or not re.match("^[a-zA-z]*$",cust_fname):
            print("Error! Only 15 characters a-z allowed.")
            cust_fname = input(" First Name : ")
    
        cust_lname = input(" Last Name(only 15 characters) : ")
        while (len(cust_lname)>15) or not re.match("^[a-zA-z]*$",cust_lname):
            print("Error! Only 15 characters a-z allowed.")
            cust_lname = input(" Last Name : ")
        cust_address = input(" Address : ")
        cust_pincode = input(" Pincode(maximum 10 digits) : ")
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
                     (cust_fname, cust_lname, cust_address, cust_pincode, cust_mobileno, email_id, cust_password))
        print("======| NEW CUSTOMER ADDED SUCCESSFULLY |======\n")
        conn.commit()

def show_all_rec():
    print("======| CUSTOMER DETAILS |======\n" )
    print(pd.read_sql_query("select cust_id as ID, cust_fname as FirstName, cust_lname as LastName,cust_address as Address , cust_pincode as Pincode, mobileno as Number, email_id as Email from customer_master", conn))
	 
	


def update_a_rec():
	print("======| UPADTE CUSTOMER DETAILS |======\n")
	curs = conn.cursor()
	cust_id = str(input("Please enter the customer ID to be updated : "))
	print("1. Change customer Address")
	print("2. Change customer CONTACT NUMBER")
	ch=input("Enter your choice: ")
	if(ch=='1'):
		n=input("enter the new customer Address: ")
		curs.execute("UPDATE customer_master set cust_address=? where cust_id = ?",[n, cust_id])
		conn.commit()
	elif(ch=='2'):
		n=input("enter the new customer contact number: ")
		curs.execute("UPDATE customer_master set mobileno=? where cust_id = ?",[n, cust_id])
		conn.commit()
	else:
		print("invalid choice....!!!")
	print("======| CUSTOMER DETAILS UPADTED SUCCESFULLY |======\n")

def delete_a_rec():
    print("======| REMOVE CUSTOMER |======\n")
    curs = conn.cursor()
    cust_id = str(input("Please enter the customer ID to be deleted : "))
    
    curs.execute("DELETE from customer_master where cust_id = ?", cust_id)
    print("======| CUSTOMER REMOVED SUCCESFULLY |======\n")
    conn.commit()


## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
	print('=============================\n')
	print('     Customer Master Maintenance  \n')
	print('=============================\n')
	print(' Please choose from the following option : ')
	print()
	print('1. ADD NEW CUSTOMER \n')
	print('2. CUSTOMER DETAILS \n')
	print('3. REMOVE CUSTOMER \n')
	print('4. UPDATE CUSTOMER DETAILS \n')
	print()
	print('0. To EXIT the program \n')

	choice = input("Please Enter Your Option : ")
	if choice == '1':
		add_rec()
	elif choice == '2':
		show_all_rec()
	elif choice == '3':
             
		delete_a_rec()
	elif choice == '4':
		update_a_rec()
	elif choice == '0':
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")
		print("Please Enter A Valid Option")
