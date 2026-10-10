import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


url = "https://www.goodreads.com/quotes"

quotes_data = []
authors_data = []
likes_data = []


while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select("div.quoteText")
    print(len(quotes))

    authors = soup.select("span.authorOrTitle")
    print(len(authors))

    likes = soup.select("a.smallText")
    print(len(likes))

    for i in quotes:
       quotes_data.append(i.text)

    for i in authors:
       authors_data.append(i.text)

    for i in likes:
        likes_data.append(i.text)


    try:
        next_pg = soup.select_one("li.a next_page")["href"]
        url = urljoin(url, next_pg)
        print(url)

    except:
        break

data = {
    "Author" : authors_data,
    "Quotes" : quotes_data,
    "Likes"  : likes_data
}

df = pd.DataFrame(data)
df.to_csv("QuotesAuthorsLikes.csv", index=False)

