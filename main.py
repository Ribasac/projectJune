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

eel.init("web")

def callback(r, audio):
    try:
        if june.check(r.recognize_google(audio)):
            juneTrigger()
            
                
    except:
        pass

def juneTriggered():
    eel.textEdit("Listening...")
    p.playsound("trigger.mp3")
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
            speakData = task.doTask(audioData)
            editAndSpeak(speakData)
        except:
            print("Sorry I did not catch it")
            editAndSpeak("Sorry i did not understand")


def editAndSpeak(speakData):
    
    eel.textEdit(speakData)
    s.speak(speakData)


@eel.expose
def listen_thread(r, mic):
    print("Start talking")
    stop_lisentening = r.listen_in_background(mic, callback)

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
