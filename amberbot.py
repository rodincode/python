'''from googlesearch import search
import requests
from bs4 import BeautifulSoup
import random
import pyttsx3
import pyaudio
import speech_recognition as sr

def speak(command):
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()

def speech_to_text():
      r = sr.Recognizer()
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.2)
        audio = r.listen(source)
      try:
        query = r.recognize_google(audio)
        query = query.lower()
        print("Did you say: ",query)
      except Exception as e:
        speak("Sorry, I can't understand.... ")
        return "no info"
      return query

speak("Hello, Maam. I am Don Jr. at your service. What can I do for you? ")
query = speech_to_text()
if "search" in query:
      speak("What do you wan to search?")
      query = input("What do you want to search::")+"wikipedia"
      links = []
      for i in search(query,tld='co.in',num=10, stop=10):
        links.append(i)
      print(links)
      #random_link = random.choice(links)
      #print(random_link)

      random_link = links[0]
      response = requests.get(random_link)
      #print(response.text)
      soup = BeautifulSoup(response.text, 'html.parser')
      for para in soup.find_all('p'):
        speak(para.text)
        print(para.text)

elif "Youtube" in query:
'''
# python + SQLITE

# WEBCRAWLER
import sqlite3
import requests
from bs4 import BeautifulSoup
import re 
# important commands of SQL
# 
# 1. SELECT : select data from a single table

# 2. ORDER BY : sorting the data

# 3. DISTINCT : finding unique rows from the table

# 4. WHERE: filter rows of a result

# 5. INSERT: insert  rows into a table

# 6. UPDATE: update existing rows

# 7. DELETE: Delete rows 

# 8. REPLACE: insert a new row or replace the existing one

## Example::
## SELECT * FROM Students 
# this command will select all values from a table called
# students.

## SELECT rollno,subject FROM Students WHERE subject="Maths"
#this will select all the students with their roll no 
# who took mathematics as a subject

## INSERT INTO students (name, roll_no,subjects,class)
# VALUES ("Mike",45,"Maths",'VII-D')
# this will insert values of student mike in a table called
# students in their respective columns.

## Make/connect to a database
db = sqlite3.connect('crawl.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS websites (url,title,canonical,content)")


url = input("Enter a url:: ")
if len(url)<1:
      url = "https://www.youtube.com"

def get_info(url):
      if 'www' in url:
        name= re.findall('ht.*://www\.(.*?)\.',url)
        name= name[0].capitalize()
        return name
      else:
        name = re.findall('ht.*://(.*?)\.',url)
        name = name[0].capitalize()
        return name
      
webname = get_info(url)
print(webname)

urls = []
urls.append(url)

def extract_content(soup):
      try:
        title = soup.title.string
      except:
        title = "Null"
      try:
        rel = soup.find('link',{'rel':'canonical'})['href']
      except:
        rel = "Null"
      try:
        content = soup.text
        content = content.replace('\n',"")
      except:
        content= "Null"
      return title, rel, content

def extract_links(soup):
      links = soup.find_all('a')
      for link in links:
            if str(link.get('href')).startswith(url)== True and link.get('href') not in urls:
                  if '.jpg' in link.get('href') or '.png' in link.get('href') or '.pdf' in link.get('href'):
                        continue 
                  else:
                        urls.append(link.get('href'))
      return (len(links))

def insert_data(data_from_url):
      url, title, rel, content = data_from_url
      cursor.execute("INSERT INTO websites (url,title,canonical,content) VALUES (?,?,?,?)",(url,title,rel,content))
      
      db.commit()  #save

counter=0
while counter<len(urls):
  print(counter,"crawling:",urls[counter])
  response = requests.get(urls[counter])
  if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        links = extract_links(soup)
        title, rel, content = extract_content(soup)
        insert_data((urls[counter],title, rel, content))
  
  counter+=1




########### REGULAR EXPRESSIONS ###################
# \n --> next line
# \d --> digit
# \t --> space of tab

speech = '''
I have a dream that one day down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification – one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.

I have a dream today.

I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed and all flesh shall see it together.
'''

import re
x = re.search('[A-Z][a-z][a-z][a-z][a-z]', speech)
print(x)

## H.W.
'''
make a program that takes platenumber as input from the user
check if the input matches with the valid number plate:
a valid number plate consists of two alphabets in the
starting followed by two numbers, then a space and then
three numbers. For eg: XX78 787 is a valid plate number.
'''



