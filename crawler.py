import requests
from bs4 import BeautifulSoup

def getNewsContent(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    r = requests.get(url, headers=header)
    
    if r.status_code != 200:
        raise "Invalid URL"
    
    recipeSoup = BeautifulSoup(r.text, "html.parser")
    
    instructions = recipeSoup.find("div", itemprop="articleBody")
    if not instructions:
        instructions = recipeSoup.find("article", itemprop="articleBody")
    if not instructions:
        instructions = recipeSoup.find("div", id="news_body_area")
    if not instructions:
        instructions = recipeSoup.find("div", id="dic_area")
    if not instructions:
        instructions = recipeSoup.find("article", class_="article")
    
    if type(instructions) == 'NoneType':
        raise "Sorry, The site is unavailable. Please Input Url with another site"
    return instructions.text