#import pywhatkit as kit
from junepackages import askTo as a

def sendWhatsapp():
    while True:
        try:
            rNumber = a.askTo("who do you wanna send the message to?")
            break
        except:
            continue
    while True:
        try:
            messagetxt = a.askTo("what is the message?")
            break
        except:
            continue
    while True:
        try:
            mhr = a.askTo("when do you wanna sent the message?")
            break
        except:
            continue
    #mhr, mmnt = mhr.split()
    print(rNumber+messagetxt)


sendWhatsapp()
#kit.sendwhatmsg(rNumber,messagetxt, mhr, mmnt)
