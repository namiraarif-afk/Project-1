import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.select("span.text")
print(len(quotes))

for i in quotes:
    quotes_data.append(i.text)

data = {
    "Quotes" : quotes_data

}

df = pd.DataFrame(data)
df.to_csv("Quotes1_data.csv", index = False )