#!/usr/bin/env python
# coding: utf-8

# In[257]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests


# # Q1

# In[258]:


# Q1
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(page.content)
headers = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])
headers


# In[ ]:





# # Q2

# In[259]:


# Q2
import pandas as pd
page = requests.get('https://www.imdb.com/chart/top')
soup = BeautifulSoup(page.content)

moviesname = []
for i in soup.find_all('td',class_="titleColumn"):
    moviesname.append(i.text.split('\n')[2])
    
#moviesname

rating = []
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.split('\n')[1])
    
#rating

yofrel = []
for i in soup.find_all('span',class_="secondaryInfo"):
    yofrel.append(i.text)
    
#yofrel

#print(len(moviesname),len(rating),len(yofrel))

df = pd.DataFrame({'Movie Name':moviesname,'Rating':rating,'Year of release':yofrel})
df_first_100 = df.head(100)
df_first_100


# In[ ]:





# # Q3

# In[260]:


# Q3
import pandas as pd
page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
soup = BeautifulSoup(page.content)

moviesname = []
for i in soup.find_all('td',class_="titleColumn"):
    moviesname.append(i.text.split('\n')[2])
    
#moviesname

rating = []
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.split('\n')[1])
    
#rating

yofrel = []
for i in soup.find_all('span',class_="secondaryInfo"):
    yofrel.append(i.text)
    
#yofrel

#print(len(moviesname),len(rating),len(yofrel))

df = pd.DataFrame({'Movie Name':moviesname,'Rating':rating,'Year of release':yofrel})
df_first_100 = df.head(100)
df_first_100


# In[ ]:





# # Q4

# In[261]:


#Q4 A.
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup = BeautifulSoup(page.content)

teams = []
for i in soup.find_all('span',class_="u-hide-phablet"):
    teams.append(i.text)
    
#teams

match = []
matches = []
points = []

toptm = soup.find('td',class_="rankings-block__banner--matches")
match.insert(0, toptm.text) 

toptp = soup.find('td',class_="rankings-block__banner--points")
match.insert(1, toptp.text)

i=2
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    match.append(i.text)
    
matches = match[0::2]
points = match[1::2]
#matches
#points

ratings = []

toptr = soup.find('td',class_="rankings-block__banner--rating u-text-right")
ratings.insert(0, toptr.text.split('\n')[1]) 
i=1
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
#ratings

#print(len(teams),len(teams),len(points),len(ratings))
print("Top 10 Men's ODI Team Rankings")
df = pd.DataFrame({'Team Name':pd.Series(teams),'Matches':pd.Series(matches),'Points':pd.Series(points),'Ratings':pd.Series(ratings)})
df_first_10 = df.head(10)
df_first_10


# In[262]:


#Q4 B.
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup = BeautifulSoup(page.content)

i=j=k=1
playname = []

tpname = soup.find('div',class_="rankings-block__banner--name-large")
playname.insert(0, tpname.text) 

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    playname.append(i.text.split('\n')[1])
    
#playname

ptname = []

tpco = soup.find('div',class_="rankings-block__banner--nationality")
ptname.insert(0, tpco.text.split('\n')[2]) 

for j in soup.find_all('span',class_="table-body__logo-text"):
    ptname.append(j.text)
    
#ptname

prat = []

tprat = soup.find('div',class_="rankings-block__banner--rating")
prat.insert(0, tprat.text) 

for k in soup.find_all('td',class_="table-body__cell rating"):
    prat.append(k.text)
    
#prat

#print(len(playname),len(ptname),len(prat))
print("Top 10 Men's ODI Batting Rankings")
df = pd.DataFrame({'Player':playname,'Team':ptname,'Rating':prat})
df_first_10 = df.head(10)
df_first_10


# In[263]:


#Q4 C.
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup = BeautifulSoup(page.content)

i=j=k=1
playname = []

tpname = soup.find('div',class_="rankings-block__banner--name-large")
playname.insert(0, tpname.text) 

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    playname.append(i.text.split('\n')[1])
    
#playname

ptname = []

tpco = soup.find('div',class_="rankings-block__banner--nationality")
ptname.insert(0, tpco.text.split('\n')[2]) 

for j in soup.find_all('span',class_="table-body__logo-text"):
    ptname.append(j.text)
    
#ptname

prat = []

tprat = soup.find('div',class_="rankings-block__banner--rating")
prat.insert(0, tprat.text) 

for k in soup.find_all('td',class_="table-body__cell rating"):
    prat.append(k.text)
    
#prat

#print(len(playname),len(ptname),len(prat))
print("Top 10 Men's ODI Bowling Rankings")
df = pd.DataFrame({'Player':playname,'Team':ptname,'Rating':prat})
df_first_10 = df.head(10)
df_first_10


# In[ ]:





# # Q5

# In[264]:


#Q5 A.
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup = BeautifulSoup(page.content)

teams = []
for i in soup.find_all('span',class_="u-hide-phablet"):
    teams.append(i.text)
    
#teams

match = []
matches = []
points = []

toptm = soup.find('td',class_="rankings-block__banner--matches")
match.insert(0, toptm.text) 

toptp = soup.find('td',class_="rankings-block__banner--points")
match.insert(1, toptp.text)

i=2
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    match.append(i.text)
    
matches = match[0::2]
points = match[1::2]
#matches
#points

ratings = []

toptr = soup.find('td',class_="rankings-block__banner--rating u-text-right")
ratings.insert(0, toptr.text.split('\n')[1]) 
i=1
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
#ratings

#print(len(teams),len(teams),len(points),len(ratings))
print("Top 10 Women's ODI Team Rankings")
df = pd.DataFrame({'Team Name':pd.Series(teams),'Matches':pd.Series(matches),'Points':pd.Series(points),'Ratings':pd.Series(ratings)})
df_first_10 = df.head(10)
df_first_10


# In[265]:


#Q5 B.
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup = BeautifulSoup(page.content)

i=j=k=1
playname = []

tpname = soup.find('div',class_="rankings-block__banner--name-large")
playname.insert(0, tpname.text) 

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    playname.append(i.text.split('\n')[1])
    
#playname

ptname = []

tpco = soup.find('div',class_="rankings-block__banner--nationality")
ptname.insert(0, tpco.text.split('\n')[2]) 

for j in soup.find_all('span',class_="table-body__logo-text"):
    ptname.append(j.text)
    
#ptname

prat = []

tprat = soup.find('div',class_="rankings-block__banner--rating")
prat.insert(0, tprat.text) 

for k in soup.find_all('td',class_="table-body__cell rating"):
    prat.append(k.text)
    
#prat

#print(len(playname),len(ptname),len(prat))

print("Top 10 Women's ODI Batting Rankings")
df = pd.DataFrame({'Player':playname,'Team':ptname,'Rating':prat})
df_first_10 = df.head(10)
df_first_10


# In[266]:


#Q5 C.
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup = BeautifulSoup(page.content)

i=j=k=1
playname = []

tpname = soup.find('div',class_="rankings-block__banner--name-large")
playname.insert(0, tpname.text) 

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    playname.append(i.text.split('\n')[1])
    
#playname

ptname = []

tpco = soup.find('div',class_="rankings-block__banner--nationality")
ptname.insert(0, tpco.text.split('\n')[2]) 

for j in soup.find_all('span',class_="table-body__logo-text"):
    ptname.append(j.text)
    
#ptname

prat = []

tprat = soup.find('div',class_="rankings-block__banner--rating")
prat.insert(0, tprat.text) 

for k in soup.find_all('td',class_="table-body__cell rating"):
    prat.append(k.text)
    
#prat

#print(len(playname),len(ptname),len(prat))
print("Top 10 Women's ODI All-Rounder Rankings")
df = pd.DataFrame({'Player':playname,'Team':ptname,'Rating':prat})
df_first_10 = df.head(10)
df_first_10


# In[ ]:





# # Q6

# In[267]:


# Q6
page = requests.get('https://coreyms.com/')
soup = BeautifulSoup(page.content)

heading = []
for i in soup.find_all('a',class_="entry-title-link"):
    heading.append(i.text)
    
print("Heading of the posts","\n",heading,"\n")

dates = []
for i in soup.find_all('time',class_="entry-time"):
    dates.append(i.text)

print("Date of the posts","\n",dates,"\n")
#dates

contents = []
for i in soup.find_all('div',class_="entry-content"):
    #contents.append(i.text)
    contents.append(i.text.split('\n')[1])
    
#contents
print("Content of the posts","\n",contents,"\n")

yurl = []
for i in soup.find_all('iframe',class_="youtube-player"):
    yurl.append(i['src'])
    
#yurl
print("Youtube URL","\n",yurl,"\n")

df = pd.DataFrame({'Heading':pd.Series(heading),'Date':pd.Series(dates),'Content':pd.Series(contents),'Youtube URL':pd.Series(yurl)})
df


# In[ ]:





# # Q7

# In[268]:


# Q7
import pandas as pd
page = requests.get('https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N%20DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8%20iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0')
soup = BeautifulSoup(page.content)

house_title = []
for i in soup.find_all('h2',class_="heading-6 font-semi-bold nb__25Cl7"):
    house_title.append(i.text)
    
#house_title
print("House Title","\n",house_title,"\n")

location = []
for i in soup.find_all('div',class_="nb__1EwQz"):
    location.append(i.text)
    
#location
print("Location","\n",location,"\n")

area = []
for i in soup.find_all('div',class_="nb__FfHqA"):
    area.append(i.text)

#area
print("Area","\n",area,"\n")

emi = []
for i in soup.find_all('div',class_="font-semi-bold heading-6",id="roomType"):
    emi.append(i.text.split('/')[0])

#emi
print("EMI\Month","\n",emi,"\n")

price = []
for i in soup.find_all('div',class_="nb__4L90a",id="minDeposit"):
    for j in i.find_all('div',class_="font-semi-bold heading-6"):
        price.append(j.text)

#price
print("Price","\n",price,"\n")

df = pd.DataFrame({'House Title':house_title,'Location':location,'Area':area,'EMI/Month':emi,'Price':price})
df


# In[ ]:





# # Q8

# In[269]:


# Q8
import pandas as pd
page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
soup = BeautifulSoup(page.content)

rest_name = []
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    rest_name.append(i.text)
    
#rest_name

cuisine = []
for i in soup.find_all('span',class_="double-line-ellipsis"):
    #cuisine.append(i.text)
    cuisine.append(i.text.split('|')[1])
    
#cuisine

location = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
#location

ratings = []
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)
    
#ratings

img_url = []
for i in soup.find_all('img',class_="no-img"):
    img_url.append(i['data-src'])
    
#img_url

#print(len(rest_name),len(cuisine),len(location),len(ratings),len(img_url))

df = pd.DataFrame({'Restaurant name':rest_name,'Cuisine':cuisine,'Location':location,'Ratings':ratings,'Image URL':img_url})
df


# In[ ]:





# # Q9

# In[270]:


#Q9
import pandas as pd
page = requests.get('https://en.tutiempo.net/delhi.html?data=last-24-hours')
soup = BeautifulSoup(page.content)

hour = []
for i in soup.find_all('div',class_='last24 thh'):
    for j in i.find_all('td'):
        hour.append(j.text)

hours = hour[0::6]
#hours

temp = []
for i in soup.find_all('td',class_="t Temp"):
    temp.append(i.text)
    
#temp

wind = []
for i in soup.find_all('td',class_="wind"):
    wind.append(i.text)
    
#wind

wc = []
for i in soup.find_all('span',class_="thhip ico i0530 u3018"):
    wc.append(i.text)
    
#wc

hum = []
for i in soup.find_all('td',class_="hr"):
    hum.append(i.text)
    
#hum

press = []
for i in soup.find_all('td',class_="prob"):
    press.append(i.text)
    
#press

#print(len(hours),len(temp),len(wind),len(wc),len(hum),len(press))

df = pd.DataFrame({'Hour':pd.Series(hours),'Temperature':pd.Series(temp),'Wind':pd.Series(wind),'Weather condition':pd.Series(wc),'Humidity':pd.Series(hum),'Pressure':pd.Series(press)})
df


# In[ ]:





# # Q10

# In[271]:


#Q10
import pandas as pd
page = requests.get('https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/')
soup = BeautifulSoup(page.content)

monu_name = []
monu_desc = []
monu_img = []
for i in soup.find_all('div',class_='blog--single__content column--3-4 u-spacing-third'):
    for j in i.find_all('p'):
        monu_desc.append(j.text)
        mdesc = monu_desc[2::3]
        for k in j.find_all('strong'):
            monu_name.append(k.text.split(',')[0])
        for l in j.find_all('img'):
            monu_img.append(l['src'])
            mimg=monu_img[1::2]

#monu_name
#mdesc
#mimg


#print(len(monu_name),len(mdesc),len(mimg))
df = pd.DataFrame({'Monument Name':pd.Series(monu_name),'Monument Description':pd.Series(mdesc),'Image URL':pd.Series(mimg)})
df_first_10 = df.head(10)
df_first_10


# In[ ]:




