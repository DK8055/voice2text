import speech_recognition as sr
import speakkk as sp
x=open("temp.txt","w+")
srrr = 48000
cz = 1024
r = sr.Recognizer()
device_id=1
sp.speak("say after 2 sec")
def takecommnd():
    with sr.Microphone(device_index=device_id, sample_rate=srrr,
                       chunk_size=cz) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        i=0
        try:
            text=None
            while text!="exit":
                audio = r.listen(source)
                i = i + 1
                text = r.recognize_google(audio, language="en-us")
                if text != None and text!="exit":
                    print(text)
                    x.write(text)
                else:
                    print("please try again")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request your input please check connecyion and try again; {0} ".format(e))
takecommnd()
x.close()
print("Please save the current lines from temp.txt,after reusing this the current work eill lost")