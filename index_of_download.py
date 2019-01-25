import requests
from bs4 import BeautifulSoup
import os

def getting_urls(url):
    r = requests.get(url)
    links_name = {}
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.find_all('a'):
        if (a['href'].split('.')[-1] == 'wav'):
            links_name[a['href']] = url +"/"+ a['href']
    return links_name

web_page_url = "http://www.wou.edu/~tbafarat06/1001%20Sound%20Effects/"
url = []

r_ = requests.get(web_page_url)
soup_ = BeautifulSoup(r_.content, 'html.parser')
for a in soup_.find_all('a'):
    url.append(web_page_url+a['href'])
    #print(web_page_url+a['href'])

for u in url:
    name = u.split('/')[-2]
    links_name = getting_urls(u)
    targer_path = '/home/amritpal/Documents/database/'+name+'/'
    if not (os.path.exists(targer_path)):
        os.mkdir(targer_path)
        for name, song_url in links_name.items():
            print(targer_path + name)
            r = requests.get(song_url)    
            with open(targer_path+name, 'wb') as f:
                f.write(r.content)
        