import math
import wikipedia
from junepackages import speak as s
from tasks import appOpen, joke, message
import eel


def calculate(audioData):
    mathData = audioData.replace("calculate", "").replace("times", "*").replace("Times", "*").replace("divided by", "/").replace("Divided by", "/").replace("divided By", "/").replace("Divided By", "/").replace("divided /", "/").replace("Divided /", "/").replace("plus", "+").replace("Plus", "+").replace("minus", "-").replace("Minus", "-")
    operation = mathData.replace("zero","0").replace("Zero","0").replace("one", "1").replace("One", "1").replace("two", "2").replace("Two", "2").replace("three", "3").replace("Three", "3").replace("four", "4").replace("Four", "4").replace("five", "5").replace("Five", "5").replace("six", "6").replace("Six", "6").replace("seven", "7").replace("Seven", "7").replace("eight", "8").replace("Eight", "8").replace("nine", "9").replace("Nine", "9")
    mathData = operation.replace(" ", "").replace("X", "*").replace("x", "*")
    if "0/0" in mathData:
        result = "Sorry it is undefined"
    else:
        result = operation + " is " + str(eval(mathData))
    return result

def whoIs(audioData):
    titleData = audioData.replace("who is ","").replace("Who is ","").replace("who ","").replace("Who ","")
    result = wikipedia.summary(titleData, sentences = 1)
    return result

def doTask(audioData, user):
    audioData =  audioData.lower()

    if any(i in audioData for i in ("add contact","add contacts")):
        eel.openContact()
        result = "Starting...."
    elif any(i in audioData for i in ("register email","add email")):
        eel.openEmail()
        result = "Starting...."

    elif user!="helper":
        if any(i in audioData for i in ("calculate","Calculate")):
            result = calculate(audioData)
        
        elif any(i in audioData for i in ("who","who is","Who","Who is")):
            result = whoIs(audioData)

        elif any(i in audioData for i in ("open", "Open")):
            result = appOpen.open(audioData)

        elif any(i in audioData for i in ("joke","Joke")):
            result = joke.getJoke()

        elif any(i in audioData for i in ("send message","message","send whatsapp")):
            message.sendWhatsapp()
            result = "Ok...."
        elif any(i in audioData for i in ("send email","an email","send an email")):
            result = message.sendEmail()
            
    return result
