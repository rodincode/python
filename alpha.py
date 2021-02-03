# combine google search+BS+request
##### CHATBOT ALPHA #####

from googlesearch import * #to get links
import requests # to enter
import bs4 as bs #to read tags
import random
import datetime
import wikipedia
# from gtts import gTTS(text to speech)
#import pyaudio# #(speech to text)
import pyttsx3
import speech_recognition as sr
import urllib.request
engine=pyttsx3.init()
voices_id="com.apple.speech.synthesis.voice.Alex"
voices=engine.getProperty("voices")
engine.setProperty("voice",voices_id)
def speak(text):
	engine.say(text)
	engine.runAndWait()
# read a para inside a random link
# get url
print("Hello I am Alpha in your service.")
speak("Hello I am Alpha in your service.")
speak("ask something")
"""
for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) 
    """

def hear():
	r = sr.Recognizer()
	with sr.Microphone() as source: 
		print("Listening....")
		r.pause_threshold =1
		audio = r.listen(source)
		return r.recognize_google(audio)
# step1: install brew
# step2: brew install portaudio
# step3: pip install pyaudio

try:
	#query=input("Type Here:: ")
	query= hear().lower()
	if "wikipedia" in query:
		results=query.replace ("wikipedia","")
		result=wikipedia.summary (query) 
		speak (result)
	elif "time" in query:
		t=("Sir the time is"+datetime.datetime.now())
		speak(t)
		'''	
	result=[]
	for i in search(query,tld='co.in',num=10,stop=10):
		result.append(i)
	print(result)
	search= random.choice(result)
	print(search)
	x=urllib.request.urlopen(search).read()
	soup=bs.BeautifulSoup(x, 'lxml')
	x=soup.find('p').getText()
	print(x)
	for paragraph in soup.find_all('p'):
		print(paragraph.text)'''

except Exception:
	print("There was some problem in listening")
	print("Say that again...")