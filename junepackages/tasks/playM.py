import pywhatkit as kit

def playYT(audioData):
    audioData = audioData.replace("play", "");
    kit.playonyt(audioData)
    result = "playing..."
    return result
