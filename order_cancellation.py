import sqlite3


def cancel_order():
	
	while True:
		cancel = input('Are You Sure To Cancel Your Order YES (y) / NO (n) : ')
		if(cancel == 'y'):
			invoice1 = open('invoice.txt','r')
			for line in invoice1:
				line = line.rstrip()
				if not line.startswith('Your '):
					continue
				word = line.split()
				amount =word[4]
			invoice1.close()	
			invoice = open('invoice.txt','w')
			invoice.write('NO ORDERS AVAILABLE')
			invoice.close()
			print()
			print('Your Order Is Successfully Cancelled')
			print()
			print('Your Money Has Been Refunded  Rs.', amount)
			print()
			feedback = input('Please Give Your Feedback Regarding To Your Cancellation : ')
			print()
			print('THANK YOU FOR YOUR VALUABLE FEEDBACK')
			break
		elif (cancel == 'n'):
			print()
			print('Your Order Will Be Deliver Soon')
			break
		else:
			print('Invalid Response')
	
	


def show_order():
	print('=================================\n')
	print('                YOUR ORDER DETAILS  \n')
	print('=================================\n')
	print("ITEM                 PRICE")
	invoice = open('invoice.txt')
	for line in invoice:
		print(line)
	invoice.close()
	

## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
	print('=================================\n')
	print('          CANCELLATION OF ORDERS \n')
	print('=================================\n')
	print(' Please choose from the following option : ')
	print()
	print('1. SHOW ORDER \n')
	print('2. CANCEL ORDER \n')
	print()
	print('0. To EXIT the program \n')

	choice = input("Please Enter your option : ")
	if choice == '1':
		show_order()
	elif choice == '2':
		cancel_order()
	elif choice == '0':
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")
