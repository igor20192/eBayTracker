import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_ebay_data(keywords):
    url = f"https://www.ebay.com/sch/i.html?_nkw={keywords}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    items = []
    for item in soup.select(".s-item"):
        title = item.select_one(".s-item__title").text
        price = item.select_one(".s-item__price").text
        link = item.select_one(".s-item__link")["href"]
        items.append({"title": title, "price": price, "link": link})

    return pd.DataFrame(items)


keywords = "Dreambox DM900"
df = get_ebay_data(keywords)
print(df)
