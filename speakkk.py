import pyttsx3
eng= pyttsx3.init('sapi5')
voicee = eng.getProperty('voices')
eng.setProperty('rate',150)
eng.setProperty('voice',voicee[1].id)
def speak(audio):
    eng.say(audio)
    eng.runAndWait()