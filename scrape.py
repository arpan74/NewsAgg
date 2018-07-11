from bs4 import BeautifulSoup
import requests, copy

def getContent():
    content = downloadPages()
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all(attrs={"class":"wsj-headline-link"}):
        i["href"] = "http://outline.com/" + i["href"]    
    return str(soup)


def downloadPages():
    source = "https://www.wsj.com"
    r = requests.get(source)
    return r.text

def checkLinks(content):
    soup = BeautifulSoup(content, 'html.parser')

    for i in soup.find_all(attrs={"class":"wsj-headline-link"}):
        print(i)


if __name__ == "__main__":
    checkLinks(getContent())
