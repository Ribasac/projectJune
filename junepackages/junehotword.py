def check(audioData):
    audioData = audioData.lower()
    print(audioData)
    hotWords = ["sajan","hey","","june","jude","hey june","hey you","hey john","John","john","une","hey tune","joe","siri","Siri", "google", "Google"]
    if any(hw in audioData for hw in hotWords):
        return True
    else:
        return False
