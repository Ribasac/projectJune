#import  mysql.connector as con
import sqlite3 as sq
from junepackages import speak as s

#mydb = con.connect(
    #host = "localhost",
    #username = "root",
    #password = "june",
    #database = "june"
    #)

def addContact(cName,cNumber,cEmail):
    try:
        #mycursor = mydb.cursor()

        #insertSql = "insert into contacts values(%s,%s,%s)"
        #values = (cName,cNumber,cEmail)
        #mycursor.execute(insertSql,values)

        con = sq.connect("contacts.db")
        iSql = "insert into contacts values('"+cName+"','"+cNumber+"','"+cEmail+"')"
        con.execute(iSql)

        #mydb.commit()
        con.commit()
        con.close()
        result = "Success"
    except:
        result = "Failed"
    return result

def fetchNumber(audioData):
    try:
        con = sq.connect("contacts.db")
        iSql = "select number from contacts where name='"+audioData+"';"
        cursor = con.execute(iSql)
        for row in cursor:
            result = row[0]
        con.close()
        return result
    except:
        s.speak("Cannot find the contact")


