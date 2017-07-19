# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:36:53 2016

@author: sunny
"""
import sqlite3
def sale_details():
    
    print('=================================\n')
    print('     Sale Details Till Date       \n')
    print('=================================\n')
    details = open('report.txt','r')
    for line in details:
        line=line.rstrip()
        print(line)
    
def search():
    print('=================================\n')
    print('   Search For A Particular Detail   \n')
    print('=================================\n')
    date = input("Enter Date DD/MM/YY : ")
    print()
    print("Date         Order ID      Customer ID         Amount\n")
    amount=0
    data = open('report.txt','r')
    for line in data:
        
        if not line.startswith(date):
            continue
        print(line)
        word = line.split()
        a=word[3]
        
        amount +=int(a)
       # print(word[3])
    data.close()	
    
    print("Total Amount                                 "+str(amount))


def total_sale():
    amount=0
    count=0
    import time
    print("Date         Order ID      Customer ID         Amount\n")
    d=time.strftime("%d/%m/%Y")
    data = open('report.txt','r')
    for line in data:
        
        
        if not line.startswith(d):
            continue
        print(line)
        count+=1
        word = line.split()
        a=word[3]
        
        amount +=int(a)
       # print(word[3])
    data.close()	
    
    print("Total Sale : ",count,"Total Amount                 "+str(amount))
    
## this is the main program

conn = sqlite3.connect('shop_master_db')

while True:
	print('=================================\n')
	print('               REPORT            \n')
	print('=================================\n')
	print(' Please choose from the following option : ')
	print()
	print('1. Sale Details \n')
	print('2. Search For Particular Detail \n')
	print('3. Current Day Total Sale \n')
	
	
	print('0. CLOSE \n')

	choice = (input("Please Enter Your Option : "))
	if choice == '1':
		sale_details()
	elif choice == '2':
		search()
	elif choice == '3':
		total_sale()
	
	elif choice == '0':
		conn.close()
		break
	else:
		print("Invalid choice ....!!!!\n")
		print("Please enter a valid option")

		