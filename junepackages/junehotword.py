def check(audioData):
    hotWords = ["Hey","hey","June","june","Jude","jude","hey june","hey you","hey john","John","john","une","hey tune","joe","Joe","siri","Siri", "google", "Google"]
    if any(hw in audioData for hw in hotWords):
        return True
    else:
        return False
