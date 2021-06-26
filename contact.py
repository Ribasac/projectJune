import sqlite3 as sq

con = sq.connect("contacts.db")

res = con.execute("delete from contacts;")


con.close()            
