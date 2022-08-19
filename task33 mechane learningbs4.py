
import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get('https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DAPPLE')
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)


names=soup.find_all('div',class_="_4rR01T")
# print(names)
name=[]
for i in names:
    d=i.get_text()
    name.append(d)
# print(name)

price=soup.find_all('div',class_="_30jeq3 _1_WHN1")
# print(prices)
prices=[]
for i in price:
    d=i.get_text()
    s=d[1:]
    prices.append(s)
# print(prices)

rate=soup.find_all('div',class_="_3LWZlK")
# print(rate)
ratings=[]
for i in rate:
    d=float(i.get_text())
    ratings.append(d)
# print(ratings)

image=soup.find_all('img',class_="_396cs4 _3exPp9")
# print(images)
images=[]
for i in image:
    d=i['src']
    images.append(d)
# print(images)



# link=soup.find_all('a',class_="_1fQZEK")
# # print(links)
# links=[]
# for i in link:
#     d='https://www.flipkart.com'+i['href']
#     links.append(d)
# print(links)

link=soup.find_all('a',class_="_1fQZEK")
# print(links)
links=[]
for i in link:
    d='https://www.flipkart.com'+i['href']
    links.append(d)


df=pd.DataFrame()

df['name of mobile']=name
df['name of price']=price
df['name of ratings']=ratings
df['name of images']=images
df['name of links']=links

# print(df)


df.to_csv('Mobiles_data.csv')


