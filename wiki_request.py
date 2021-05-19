import requests
from bs4 import BeautifulSoup
import pandas as pd
import wikipedia
import json

def scrape_wiki_package(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text)
    title = soup.find('h1',{"class": "firstHeading"}).text
    r = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&titles='+title+'&format=json')
    json2 = json.loads(r.text)
    pageid = 0
    for key in json2['query']['pages'].keys():
        pageid = key
    return wikipedia.page(pageid=pageid).summary

def scrape_wiki(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text)
    #title = soup.find({"class": "firstheading"})
    content = []

    if soup.find("div", {"class": "toclimit-3"}) is not None:
        tag = soup.find("div", {"class": "toclimit-3"})
    else:
        tag = soup.find("div", {"class": "toc"})

    for h2 in tag.findAllNext(['h2','h3']):
        if 'h2' in h2.name:
            h2text = h2.text
            pass
        elif 'h3' in h2.name:
            for h3 in h2.findAllNext(['p','h3']):
                if 'h3' in h3.name:
                    break
                elif 'p' in h3.name:
                    content.append((h2.text,h3.text))

    df = pd.DataFrame(content,columns=['Topic','text'])
    datadump = ''

    for index, row in df.head(2).iterrows():
        datadump = datadump + row['text']
    return datadump