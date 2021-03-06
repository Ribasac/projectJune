import eel
import speech_recognition as sr
import time
import threading
from gtts import gTTS
import os
import playsound as p
from junepackages import speak as s
from junepackages import task
from junepackages import junehotword as june
from junepackages import user, contacts
from pygame import mixer


eel.init("web")

#username = "Ribas"
username = user.login()
print(username)
triggerFlag=True
mixer.init()
mixer.music.load("trigger.mp3")


def callback(r, audio):
    try:
        if june.check(r.recognize_google(audio)):
            juneTrigger()
            
                
    except:
        triggerFlag=True
        pass

def juneTriggered():
    triggerFlag=False
    eel.textEdit("Listening...")
    s.speak("Listening...")
    #p.playsound("trigger.mp3")
    #mixer.music.play()
    print("Triggered")

@eel.expose
def juneTrigger():
    listenAudio()

def listenAudio():
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        juneTriggered()
        try:
            audio = r.listen(source)
            audioData = r.recognize_google(audio)
            eel.textEdit(audioData)
            print(audioData)
            speakData = task.doTask(audioData, username)
            s.speak(speakData)
            triggerFlag=True
        except:
            print("Sorry I did not catch it")
            s.speak("Sorry i did not understand")
            triggerFlag=True

@eel.expose
def forceTask(audioData):
    speakData = task.doTask(audioData, username)
    s.speak(speakData)

def editAndSpeak(speakData):
    
    eel.textEdit(speakData)
    s.speak(speakData)

@eel.expose
def sendContact(cName,cNumber,cEmail):
    result = contacts.addContact(cName,cNumber,cEmail)
    eel.pyAlert(result)

@eel.expose
def sendEmail(eEmail,ePassword):
    result = email.addEmail(eEmail,ePassword)
    eel.pyAlert(result)

@eel.expose
def listen_thread(r, mic):
    print("Start talking")
    stop_lisentening = r.listen_in_background(mic, callback)
    eel.userSet(username)

def app_window():
    eel.init("web")
    eel.start("index.html", size=(1600,768), position=(50,50))
  

r = sr.Recognizer()
mic = sr.Microphone()


appThread = threading.Thread(target = app_window)
listenThread = threading.Thread(target = listen_thread , args = (r, mic)) 


with mic as source:
    r.adjust_for_ambient_noise(source)

appThread.start()
listenThread.start()

while True:
    time.sleep(0.1)
