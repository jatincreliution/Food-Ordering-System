import sqlite3
import pandas as pd

def menu():

    print("======| MENU FOR DIFFERENT SHOPS |======\n" )
    print("======| GOLDEN GATE |======\n" )    
    print(pd.read_sql_query("select item_id,item_name,item_price from shop_menu where shop_id=1", conn))
    print("======| BELLAGIO |======\n" )	
    print(pd.read_sql_query("select item_id,item_name,item_price from shop_menu where shop_id=2", conn))
    print("======| BAWARCHI |======\n" )
    print(pd.read_sql_query("select item_id,item_name,item_price from shop_menu where shop_id=3", conn))

	
def order():
    curs = conn.cursor()
    print("======| WE ARE HAPPY TO SERVE YOU |======\n" )
    print()
    file = open('invoice.txt','w')
    amount = 0
    file1 = open('login.txt')
    for i in file1:
        cust_id=i
        line1="Customer ID : "+i
    l = '==========CASH MEMO=========='
    
    file.write(l)
    file.write('\n')
    import time
    d1=time.strftime("%d%m%Y")
    order_id = cust_id+""+d1
    file.write("Order ID"+"   "+order_id)
    file.write('\n')
    file.write(line1+"     ")
    d=time.strftime("%d/%m/%Y")
    file.write("Date : "+d)
    file.write('\n')
    line2 = "ITEM   QUANTITY    PRICE"
    file.write(line2)
    file.write('\n')
    file1.close()
    while(True):
    		item_id =	str(input("\nEnter Item Id To Add Item : "))
    		quantity = int(input("\nEnter Quantity : "))
    		curs.execute("select item_price from shop_menu where item_id=? ",(item_id))
    		price = curs.fetchall()
    		
    		for item in price:
       			for  p in item:
    				
           				amount += p*quantity
    		curs.execute("select item_name from shop_menu where item_id=? ",(item_id))
    		bill = curs.fetchall()
    		for row in bill:
    			line = "  :  ".join(row)
    		curs.execute("select item_price from shop_menu where item_id=? ",(item_id))
    		bill1 = curs.fetchall()
    		for row in bill1:
    			for a in row:
    				c =a
    		c=c*quantity
    		c=str(c)
    		line = line+"	  "+str(quantity)+"	  "+c
    		file.write(line)
    		file.write('\n')		
    		decision = input("CONTINUE ORDERING [YES (y) / NO (n)] : ")
    		if (decision == 'n'):
    			break
   
	
    print("\nYour Grand Total : " , amount)
    line1 ="Your Grand Total : "+str(amount)
    file.write(line1)
    file.close()
    f=open('report.txt','a')
    f.write('\n')
    
    f.write('\n')
    data = d+"    "+order_id+"           "+cust_id+"          "+str(amount)
    f.write(data)
    f.write('\n')
    f.close()
    print()
    print("======| THANK YOU FOR ORDERING !!  VISIT AGAIN !!|======\n" )


def payment():
    pay = input("MAKE PAYMENT YES(y) / NO(n) : \n")
    invoice1 = open('invoice.txt','r')
    for line in invoice1:
        line = line.rstrip()
        if not line.startswith('Your '):
            continue
        word = line.split()
        amount =word[4]
    invoice1.close()	
    print()
    if (pay == 'y'):
        print("PAYMENT SUCCESSFULL FOR Rs. ",amount)
        print('\n YOUR ORDER WILL BE DELIVERED SOON')
    elif (pay == 'n'):
        print("PAYMENT NOT DONE YET")
    else:
        print('Invalid Response')


def invoice():
	print('=================================\n')
	print('             INVOICE             \n')
	print('=================================\n')
	
	invoice = open('invoice.txt')
	for line in invoice:
		print(line)
	invoice.close()


## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
	print('=================================\n')
	print('          CUSTOMER ORDERING \n')
	print('=================================\n')
	print(' Please choose from the following option : ')
	print()
	print('1. MENU \n')
	print('2. ORDER \n')
	print('3. INVOICE \n')
	print('4. PAYMENT \n')
	print()
	print('0. To EXIT the program \n')

	choice = input("Please Enter your option : ")
	if choice == '1':
		menu()
	elif choice == '2':
		order()
	elif choice == '3':
		invoice()
	elif choice == '4':
		payment()
	
	elif choice == '0':
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")
0
