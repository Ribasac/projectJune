from gtts import gTTS
import os
import playsound

fileNumber = 1

def speak(speakData):
    global fileNumber
    tts = gTTS(text=speakData)
    fileName = "audio"+str(fileNumber)+".mp3"
    tts.save(fileName)
    playsound.playsound(fileName)
    os.remove(fileName)
    fileNumber = fileNumber+1
