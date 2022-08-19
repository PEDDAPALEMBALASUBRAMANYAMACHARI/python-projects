from numpy import append
import requests
import pandas as pd
from bs4 import BeautifulSoup
page_num=input('enter page number')
for i in range(1,int(page_num)+1):
    response=requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&otracker=nmenu_sub_Electronics_0_Realme&page='+str(i))
# print(response)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

names=soup.find_all('div',class_="_4rR01T")
# print(names)
name=[]
for i in names:
    d=i.get_text()
    name.append(d)
    # print(names)

prices=soup.find_all('div',class_="_3I9_wc _27UcVY")
price=[]
for i in prices:
    d=i.get_text()
    j=d[1:]
    price.append(j)
    # print(price)
ratings=soup.find_all('div',class_="_3LWZlK")
rating=[]
for i in ratings:
    d=float(i.get_text())
    rating.append(d)
    # print(ratings)
images=soup.find_all('img',class_="_396cs4 _3exPp9")
image=[]
for i in images:
    d=i['src']
    image.append(d)
    # print(images)
links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in link:
    d='https://www.flipkart.com'+i['href']
    links.append(d)
    # print(links)

df=pd.DataFrame()

df['mobile Names']=names
df['mobile Prices']=prices
df['mobile Ratings']=ratings
df['mobile Images']=images
df['mobile Links']=links
# print(df)
df.to_csv('mobiles_data2.csv')


















