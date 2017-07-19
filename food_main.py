#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:46:19 2016
@author: roshni
"""
import sqlite3
import pandas as pd
import re
def login():
    username = input(" Enter Email ID : ")  
    password = input(" Enter Password : ")
    curs=conn.cursor()
    curs.execute(" select cust_id from customer_master where email_id =? and password =?",(username,password))
    lst = curs.fetchall()
    for tup in lst:
        for element in tup:
            cust_id = str(element)
            
    
    if(len(lst)>0):
        login=open('login.txt','w')
        
        login.write(cust_id)
        login.close()
        while True:
            print('=============================\n')
            print('FOOD ORDERING APPLICATION\n')
            print('=============================\n')
            print(' Please choose from the following option : ')
            print()
            print('1. Shop Master Maintenance \n' )
            print('2. Shop Menu Master Maintenance \n')
            print('3. Customer Master Maintenance \n')
            print('4. Customer Ordering \n')
            print('5. Cancellation Of Order \n')
            print('6. Report \n')
            print('0. Logout \n')
        
            choice = (input("Please Enter your option : "))
            if choice == '1':
                with open('shop_master.py') as source_file:
                        exec(source_file.read())
            elif choice == '2':
                with open('shop_menu_master.py') as source_file:
                        exec(source_file.read())
            elif choice == '3':
                with open('customer_master.py') as source_file:
                        exec(source_file.read())
            elif choice == '4':
                with open('customer_ordering.py')as source_file:
                        exec(source_file.read())
            elif choice == '5':
                with open('order_cancellation.py') as source_file:
                        exec(source_file.read())
            elif choice == '6':
                with open('report.py') as source_file:
                        exec(source_file.read())
            elif choice == '0':
                break
            else:
                print("INVALID CHOICE\n")
    else:
        print("Email ID/Password Incorrect")
        print("Login Denied")
    
def show_menu():
    print("======| MENU FOR DIFFERENT SHOPS |======\n" )
    print("     ======| GOLDEN GATE |======\n" )    
    print(pd.read_sql_query("select item_id,item_name,item_price from shop_menu where shop_id=1", conn))
    print("\n     ======| BELLAGIO |======\n" )	
    print(pd.read_sql_query("select item_id,item_name,item_price from shop_menu where shop_id=2", conn))
    print("\n     ======| BAWARCHI |======\n" )
    print(pd.read_sql_query("select item_id,item_name,item_price from shop_menu where shop_id=3", conn))
def new_user():
        print("======| Please enter the Customer Details |======")
        
        cust_fname = input(" First Name (only 15 characters): ")
        while (len(cust_fname)>15) or not re.match("^[a-zA-z]*$",cust_fname):
            print("Error! Only 15 characters a-z allowed.")
            cust_fname = input(" First Name : ")
    
        cust_lname = input(" Last Name (only 15 characters): ")
        while (len(cust_lname)>15) or not re.match("^[a-zA-z]*$",cust_lname):
            print("Error! Only 15 characters a-z allowed.")
            cust_lname = input(" Last Name : ")
        cust_address = input(" Address : ")
        cust_pincode = input(" Pincode(maximun 10 characters) : ")
        while (len(cust_pincode)>10) or not re.match("^[0-9]*$",cust_pincode):
            print("Error! Only 10 digits allowed")
            cust_pincode = int(input(" Pincode : "))
        cust_mobileno = input(" Mobile Number(10 digits) : ")
    
        while (len(cust_mobileno)!=10):
            print("Error! Only 10 digits 0-9 allowed.")
            cust_mobileno = input(" Mobie Number :")
        email_id = input(" Email ID : ")
        if not re.match("[a-z0-9]\S*@\S*[a-z]", email_id):
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
	
	print('0. CLOSE \n')

	choice = (input("Please Enter Your Option : "))
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

