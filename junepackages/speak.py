from gtts import gTTS
import os
import playsound
import eel

fileNumber = 1

def speak(speakData):
    global fileNumber
    tts = gTTS(text=speakData)
    fileName = "audio"+str(fileNumber)+".mp3"
    tts.save(fileName)
    playsound.playsound(fileName)
    eel.textEdit(speakData)
    os.remove(fileName)
    fileNumber = fileNumber+1
