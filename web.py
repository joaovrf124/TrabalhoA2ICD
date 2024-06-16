from bs4 import BeautifulSoup
import requests

def getWeb(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "lxml")
    price = soup.find_all("div", class_="lister-item-content")
    return price

print(getWeb("https://www.imdb.com/title/tt16283824/reviews/?ref_=tt_ov_rt"))