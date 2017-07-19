import sqlite3
import pandas as pd
import re
def add_rec():
		
        print("======| Please enter the ITEM Details |======")
        shop_id=input("Shop Id (only 2 characters) : ")
        while (len(shop_id)>2) or not re.match("^[0-9]*$",shop_id):
            print("Error! Only 2 characters 0-9 allowed.")
            shop_id=input("Shop Id (only 2 characters) : ")
        item_name=input("Item Name (only 15 characters): ")
        while (len(item_name)>15):
            print("Error! Only 15 characters allowed.")
            item_name=input("Item Name (only 15 characters) : ")
        item_price=input("Item Price (only 4 characters) : ")
        while (len(item_price)>4) or not re.match("^[0-9]*$",item_price):
            print("Error! Only 4 characters 0-9 allowed.")
            item_price=input("Item Price (only 4 characters) : ")
            		
            
        curs = conn.cursor()
        curs.execute("INSERT INTO shop_menu(shop_id,item_name,item_price) values (?,?,?)",( shop_id, item_name, item_price))
        print("======| NEW ITEM ADDED SUCCESSFULLY |======\n")
        conn.commit()
		
        
def show_all_rec():
	
    print("======| MENU FOR DIFFERENT SHOPS |======\n" )
    print("======| GOLDEN GATE |======\n" )    
    print(pd.read_sql_query("select item_id as ItemId,item_name as Name,item_price as Price from shop_menu where shop_id=1", conn))
    print("======| BELLAGIO |======\n" )	
    print(pd.read_sql_query("select item_id as ItemId,item_name as Name,item_price as Price from shop_menu where shop_id=2", conn))
    print("======| BAWARCHI |======\n" )
    print(pd.read_sql_query("select item_id as ItemId,item_name as Name,item_price as Price from shop_menu where shop_id=3", conn))
	#curs = conn.cursor()
	#curs.execute("select item_id, item_name, item_price from shop_menu where shop_id=1 ")
	#row=curs.fetchall()
	#for rows in row:
	#	print(rows)
	#print("======| BELLAGIO |======\n" )
	#curs.execute("select item_id, item_name, item_price from shop_menu where shop_id=2 ")
	#row=curs.fetchall()
	#for rows in row:
	#	print(rows)
	#print("======| BAWARCHI |======\n" )
	#curs.execute("select item_id, item_name, item_price from shop_menu where shop_id=3 ")
	#row=curs.fetchall()
	#for rows in row:
	#	print(rows)
def update_a_rec():
	print("======| UPADTE ITEM |======\n")
	curs = conn.cursor()
	item_id=str(input("Enter Item Id To Be Updated: "))
	print("1. Change Item Name")
	print("2. Change Item Price")
	ch=input("Enter Your Choice: ")
	if(ch=='1'):
		n=input("enter the New Item Name: ")
		curs.execute("UPDATE shop_menu set item_name=? where item_id = ?",[n, item_id])
		conn.commit()
	elif(ch=='2'):
		n=input("Enter the New Price: ")
		curs.execute("UPDATE shop_menu set item_price=? where item_id = ?",[n, item_id])
		conn.commit()
	else:
		print("Invalid choice....!!!!")
	print("======| ITEM DETAILS UPADTED SUCCESFULLY |======\n")
	
													
		

def delete_a_rec():
	curs = conn.cursor()
	print("======| DELETE ITEM |======\n")
	item_id = str(input("Please enter the Item ID to be deleted : "))
	curs.execute("DELETE from shop_menu where item_id = ?", item_id)
	conn.commit()
	print("======| ITEM DELETED SUCCESFULLY |======\n")
	conn.commit()
	


## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
	print('=================================\n')
	print('  SHOP MENU MASTER MAINTENANCE  \n')
	print('=================================\n')
	print(' Please choose from the following option : ')
	print()
	print('1. ADD ITEM \n')
	print('2. SHOW MENU \n')
	print('3. DELETE ITEM \n')
	print('4. UPDATE ITEM \n')
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
		print("Please enter a valid option")
