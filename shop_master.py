import sqlite3
import re
import pandas as pd

def add_rec():
		print("======| Please enter the Shop Details |======")
		shop_name=input("Shop Name (only 15 characters) : ")
		while (len(shop_name)>15) or not re.match("^[a-zA-z\s]*$",shop_name):
			print("Error! Only 15 characters a-z allowed.")
			shop_name = input(" Shop Name (only 15 characters) : ")
		shop_location=input("Shop Location  (only 20 characters): ")
		shop_contactno=input("Contact Number is(only 10 characters) : ")
		while (len(shop_contactno)!=10) or not re.match("^[0-9]*$",shop_contactno):
			print("Error! Only 10 digits allowed.")
			shop_contactno=input("Contact Number is(only 10 characters) : ")
		shop_cuisinetype=input("Cuisine Type (only 15 characters) : ")

		curs = conn.cursor()
		curs.execute("INSERT INTO shop_master (shop_name,shop_location,shop_contactno,shop_cuisinetype) values (?,?,?,?)",(shop_name, shop_location, shop_contactno, shop_cuisinetype))
		print("\n======| NEW SHOP ADDED SUCCESSFULLY |======\n")
		conn.commit()
        
def show_all_rec():
    print("======| SHOP DETAILS |======\n" )
    print()
    print(pd.read_sql_query("select shop_id as ShopID,shop_name as Name,shop_location as Location, shop_contactno as Number,shop_cuisinetype as CuisineType from shop_master ", conn))
    print()
	
def update_a_rec():
    
    print("======| UPADTE SHOP |======\n")
    curs = conn.cursor()
    shop_id = str(input("Please enter the Shop ID to be updated : "))
	
    print("1. Change Shop Name")
    print("2. Change Shop Contact Number")
    ch=input("Enter your choice: ")
    if(ch=='1'):
    	n=input("enter the New Shop Name: ")
    	curs.execute("UPDATE shop_master set shop_name=? where shop_id = ?",[n, shop_id])
    	conn.commit()
    elif(ch=='2'):
    	n=input("enter the New Shop Contact Number: ")
    	curs.execute("UPDATE shop_master set shop_contactno=? where shop_id = ?",[n, shop_id])
    	conn.commit()
    else:
    	print("Invalid choice....!!!!")
    print("======| SHOP DETAILS UPADTED SUCCESFULLY |======\n")

def delete_a_rec():
	print("======| DELETE SHOP |======\n")
	curs = conn.cursor()
	shop_id = str(input("Please enter the Shop ID to be deleted : "))
	curs.execute("DELETE from shop_master where shop_id = ?", shop_id)
	print("======| SHOP DELETED SUCCESFULLY |======\n")
	conn.commit()


## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
    print('=============================\n')
    print('  SHOP MASTER MAINTENANCE  \n')
    print('=============================\n')
    print(' Please choose from the following option : ')
    print()
    print('1. ADD SHOP \n')
    print('2. SHOP DETAILS \n')
    print('3. DELETE SHOP \n')
    print('4. UPDATE SHOP DETAILS \n')
    print()
    print('0. EXIT SHOP MASTER \n')
    
    choice = input("Please Enter your option : ")
    if choice == '1':
        add_rec()
    elif choice == '2':
        show_all_rec()
    elif choice == '3':
        show_all_rec()
        delete_a_rec()
    elif choice == '4':
        show_all_rec()
        update_a_rec()
    elif choice == '0':
    	conn.close()
    	break
    else:
    	print("Invalid choice ....!!!!\n")
    	print("Please enter a valid option")
