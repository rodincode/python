import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime

def speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.say(audio) 
    engine.runAndWait()

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    try:
        query= r.recognize_google(audio)
        query = query.lower()
        print("Did you say: ",query)
    except Exception:
        speak("Sorry, I can't understand...")
        return "no info"
    return query


# os -- > operating system
speak("Hello Sir, I am Don Jr. \
    at your service. What can \
        I do for you? ")

query = speech_to_text()
print(query)
if "search" in query:
     ### Web Scrapping###
     pass

elif "time" in query:
    print("The Time is", datetime.datetime.now())

