import requests
from bs4 import BeautifulSoup

def getPage(url):
    page =  requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def getDeadline(soup):
    return soup.find_all('td', class_='dateColumn')[0].get_text()
def getNotification(soup):
    return soup.find_all('td', class_='dateColumn')[1].get_text()
def getStart(soup):
    return soup.find_all('td', class_='dateColumn')[2].get_text()
def getEnd(soup):
    return soup.find_all('td', class_='dateColumn')[3].get_text()

def getVenue(soup):
    return soup.find('td', class_='locationColumn').get_text()

def getConfs(url):
    soup = getPage(url)
    confs = soup.find_all('tr', class_='heightEqualButton')
    info = dict()
    for c in confs:
        name = c.find('td', class_='nameColumn').find('a').get_text()
        info[name] =dict()
        info[name]['deadline'] = getDeadline(c)
        info[name]['notification'] = getNotification(c)
        info[name]['start'] = getStart(c)
        info[name]['end'] = getEnd(c)
	info[name]['venue'] = getVenue(c)

    return info
 
def getCats():
    soup = getPage("http://www.confsearch.org/confsearch/")
 
    categories = dict()
    for a in soup.find_all('a', href=True):
        if '/confsearch/faces/pages/topic.jsp' in a['href']: 
            categories[a.get_text()] = a['href']
            #print a['href'], a.get_text()
     
    return categories
