from bs4 import BeautifulSoup
import requests

# pip install bs4
# pip install requests

url = "https://www.imdb.com/title/tt0080684/?ref_=nv_sr_srsg_0"

response = requests.get(url)
#print(response.status_code)
#print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
title = soup.find("div", class_ = "title_wrapper")
title = title.find('h1').text
cast =  soup.find_all("div", class_ = "credit_summary_item")
cast = cast[2]
print(cast)
#cast = soup.find('a').string

# summary = soup.find("div", class_ = "summary_text").contents[0].string
# print("Movie Name:: ",title)
# print("Cast:: ",cast)
# print("Summary:: ",summary)

# Get the title and cast 
#  