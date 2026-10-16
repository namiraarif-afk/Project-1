import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags_data = [] 

tag = soup.select("a.tag")
print(len(tag))

for i in tag:
    tags_data.append(i.text)

data = {
    "Tags" : tags_data
}

df = pd.DataFrame(data)
df.to_csv("Tags_data.csv", index = False )