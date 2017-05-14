import pandas as pd
import MySQLdb					   #You must have pandas and MySQLdb packages preinstalled to continue

path='C:\Users\atulac\Desktop\DB.xlsx'             #replace this with your excel file location

backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

for key,value in backslash_map.items():
        path=path.replace(key,value)

df=pd.read_excel(path)

db = MySQLdb.connect("localhost","root","","THIRD_YEAR") # the second parameter is username, the third is password and fourth is database name.

df.to_sql('authentication_table', db, flavor='mysql', schema=None, if_exists='replace', index=False, index_label=None, chunksize=None, dtype=None)
								#authentication_table is the name of the table we want to create.

