import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


url = "https://quotes.toscrape.com/page/10/"

quotes_data = []
authors_data = []


while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select("span.text")
    print(len(quotes))

    authors = soup.select("small.author")
    print(len(authors))

    for i in quotes:
       quotes_data.append(i.text)

    for i in authors:
       authors_data.append(i.text)


    try:
        previous_pg = soup.select_one("li.previous a")["href"]
        url = urljoin(url, previous_pg)
        print(url)

    except:
        break

data = {
    "Author" : authors_data,
    "Quotes" : quotes_data

}

df = pd.DataFrame(data)
df.to_csv("QuotesDataOppositeFull.csv", index=False)
