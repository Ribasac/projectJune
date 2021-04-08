from junepackages import speak as s
from gtts import gTTS
import speech_recognition as sr

def askTo(audioData):
    print(audioData)
    s.speak(audioData)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        result = r.recognize_google(audio)
    return result
