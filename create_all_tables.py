## this program creates all required Tables in Bank System in 'bank' database
import sqlite3

conn = sqlite3.connect('shop_master_db')
curs = conn.cursor()

## to create shop_master table
#curs.execute('''DROP TABLE shop_master''')

sqlcmd ='CREATE TABLE shop_master(shop_id integer primary key, shop_name char(15), shop_location char(20), shop_contactno integer(10),shop_cuisinetype char(15))'
curs.execute(sqlcmd)
print("SHOP MASTER TABLE CREATED\n")

## to create shop_menu table
#curs.execute('''DROP TABLE shop_menu''')

sqlcmd = 'CREATE TABLE shop_menu (item_id integer primary key,shop_id integer,item_name char(15),item_price interger(4))'
curs.execute(sqlcmd)
print("SHOP MENU MASTER TABLE CREATED\n")

## to create customer_master table
#curs.execute('''DROP TABLE customer_master''')

'''sqlcmd = 'CREATE TABLE customer_master (cust_id integer primary key, cust_fname char(20), cust_lname char(20),' \
         'cust_address char(30), cust_pincode integer(8), mobileno integer(10),email_id char(50),cust_password char(10))'''
sqlcmd = 'create table customer_master (cust_id integer primary key, cust_fname char(20), cust_lname char(20),' \
         'cust_address char(30), cust_pincode integer(8), mobileno integer(10), email_id char(20), password password)'

		 
curs.execute(sqlcmd)
print("CUSTOMER MASTER TABLE CREATED\n")
conn.commit()



