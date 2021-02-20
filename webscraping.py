import bs4
import requests

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('#mediaTab_heading_0 > a > span > div:nth-child(2) > span.a-size-base.mediaTab_subtitle')

print(elems[0].text)
print(elems[0].text.strip())


def getAmazonPrice(ProductUrl):
    res = requests.get(ProductUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is '+ price)