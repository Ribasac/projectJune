import speech_recognition as sr

r=sr.Recognizer();
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("got here")
    audio = r.listen(source)
    print("got")
    audio_data = r.recognize_google(audio)
    print("here")
    print(audio_data)


