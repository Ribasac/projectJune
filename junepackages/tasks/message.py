import pywhatkit as kit
from junepackages import askTo as a
from junepackages import speak as s
from junepackages import contacts as c
import datetime as d
import threading
import eel
import smtplib, ssl


try:
    usrFile = open("emailInfo.txt", "rt");
    usrFileCheck = True
    usrInfo = usrFile.read().split("#")
    usremail = usrInfo[0]
    passwd = usrInfo[1]
    
except:
    usrFileCheck=False


def askWhatsapp():
    global rNumber,messagetxt, mhr, mmnt
    while True:
        try:
            rName = a.askTo("who do you wanna send the message to?")
            rNumber = c.fetchNumber(rName)
            print(rName)
            break
        except:
            s.speak("Did not get you")
            continue
    while True:
        try:
            messagetxt = a.askTo("what is the message?")
            print(messagetxt)
            break
        except:
            s.speak("Did not get you")
            continue

    timeNow = d.datetime.now()
    mhr = int(timeNow.strftime("%H"))
    mmnt = int(timeNow.strftime("%M"))+2

    print("here")

def whatsApp():
    kit.sendwhatmsg(rNumber,messagetxt, mhr, mmnt)

def sendWhatsapp():
    askWhatsapp()
    wThread = threading.Thread(target = whatsApp)
    wThread.start()

def sendEmail():
    try:
        if usrFileCheck :
            while True:
                try:
                    rName = a.askTo("who do you wanna send the message to?")
                    rEmail = c.fetchEmail(rName)
                    print(rName)
                    break
                except:
                    s.speak("Did not get you")
                    continue
            while True:
                try:
                    emailtxt = a.askTo("what is the email message?")
                    print(emailtxt)
                    break
                except:
                    s.speak("Did not get you")
                    continue
            
            port = 465
            server = smtplib.SMTP_SSL("smtp.gmail.com", port)
            print(server)
            server.login(usremail, passwd)
            print(rEmail)
            sendem = server.sendmail(usremail, rEmail, emailtxt)
            print(sendem)
            result = "Successfully sent"
            
        else:
            s.speak("You have not registered your email info. Register to send email.")
            eel.openEmail()

        result = " "

    except:

        result = "Failed to send"

    return result

    



