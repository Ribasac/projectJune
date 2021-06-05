import  mysql.connector as con
from junepackages import askTo as a
from junepackages import speak as s
import time

mydb = con.connect(
    host = "localhost",
    username = "root",
    password = "june"
    )

usrFile = open("info.txt", "rt");
usrFileCheck = True
usrInfo = usrFile.read().split("#")
usrname = usrInfo[0]
passwd = usrInfo[1]
print(passwd)




def login():
    if usrFileCheck :
        usr = askPass()
    else :
        usr = register()
    return usr

def register():
    s.speak("You have not registered yet. Register to continue.")
    print("........")
    time.sleep(5)
    usrname = a.askTo("What is the username?")
    passwd = a.askTo("What is the password?")
    userData = usrname + passwd
    ufw = open("info.txt", "w");
    ufw.write(userData)
    return usrname

def askPass():
    s.speak("login to continue.")
    while True:
        passkey = a.askTo("Please say the password")
        passkey = passkey.replace("L","l").replace("M","m").replace(" ","")
        print(passkey)
        if (passkey == passwd):
            s.speak("starting")
            break
        s.speak("Wrong password. Try again")
    return usrname

login()
    

