import  mysql.connector as con
from junepackages import askTo as a
from junepackages import speak as s
import time
from passlib.context import CryptContext
import os.path
import eel
from os import path

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

mydb = con.connect(
    host = "localhost",
    username = "root",
    password = "june"
    )
try:
    usrFile = open("info.txt", "rt");
    usrFileCheck = True
    usrInfo = usrFile.read().split("#")
    usrname = usrInfo[0]
    passwd = usrInfo[1]
    hpasswd = usrInfo[2]
    
except:
    usrFileCheck=False


def login():
    if usrFileCheck :
        usr = askPass()
    else :
        usr = register()
    return usr

def register():
    s.speak("You have not registered yet. Register after setup to continue.")
    print("Setting up....")
    time.sleep(5)
    usrname = a.askTo("What is the username?")
    passwd = pwd_context.encrypt(a.askTo("What is the password?").lower().replace(" ",""))
    hpasswd = pwd_context.encrypt(a.askTo("What is the password for helper?").lower().replace(" ",""))
    userData = usrname + "#" + passwd + "#" + hpasswd
    ufw = open("info.txt", "w");
    ufw.write(userData)
    return usrname

def askPass():
    s.speak("login to continue.")
    while True:
        passkey = a.askTo("Please say the password")
        passkey = passkey.lower().replace(" ","")
        print(passkey)
        if pwd_context.verify(passkey, passwd):
            name = usrname
            s.speak("starting")
            break
        if pwd_context.verify(passkey, hpasswd):
            name = "helper"
            s.speak("starting")
            break
        s.speak("Wrong password. Try again")
        time.sleep(2)
    return name

@eel.expose
def registerEmail(eEmail, ePassword):
    try:
        if not path.exists("emailInfo.txt"):
            emailData = eEmail + "#" + ePassword
            efw = open("emailInfo.txt", "w");
            efw.write(emailData)
            result = "Registered succesfully"
        else:
            result = "Already registered"
    except:
        result = "Something went wrong!"

    time.sleep(5)
    s.speak(result)
        

