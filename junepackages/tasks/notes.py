import sqlite3 as sq
from junepackages import speak as s
import datetime as d

def addNote(audioData):
    try:
        audioData = audioData.replace("add note","").replace("remember that","").replace("remember","").replace("note that","").replace("note that","")
        con = sq.connect("notes.db")
        timeNow = d.datetime.now()
        ndate = timeNow.strftime("%H")+timeNow.strftime("%M")
        iSql = "insert into notes(content,date)values('"+audioData+"','"+ndate+"')"
        con.execute(iSql)
        con.commit()
        con.close()
        result = "Success"
        return result
    except:
        result = "Error occured"
        return result

def fetchNote(audioData):
    try:
        audioData = audioData.replace("what did i tell you about","").replace("where did i","").replace("what did i","")
        content, *middle = audioData.split()
        
        con = sq.connect("notes.db")
        iSql = "select content from notes where content LIKE '%"+content+"%' order by noteid desc;"
        cursor = con.execute(iSql)
        for row in cursor:
            result = "I remember you saying " + row[0]
        con.close()
        return result
    except:
        result = "Cannot find the note"
        return result
        
