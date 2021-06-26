import pywhatkit as kit
from junepackages import askTo as a
from junepackages import speak as s
from junepackages import contacts as c
import datetime as d
import threading


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




