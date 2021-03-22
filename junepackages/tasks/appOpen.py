import os

def open(audioData):
    keyopen, *middle, appName = audioData.split()
    result = "Opening "+appName
    os.system("start "+appName)
    print("Here")
    return result

