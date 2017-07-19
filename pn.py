#!/usr/bin/env python

import sqlite3
import pandas as pd
def show_all_rec():
	print(pd.read_sql_query("select * from shop_menu", conn))
## this is the main program
conn = sqlite3.connect('./shop_master_db')
show_all_rec()
