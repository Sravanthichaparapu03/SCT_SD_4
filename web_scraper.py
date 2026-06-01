import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

books = soup.find_all("article", class_="product_pod")

for book in books:
    name = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    rating = book.p["class"][1]

    products.append({
        "Name": name,
        "Price": price,
        "Rating": rating
    })

df = pd.DataFrame(products)

df.to_csv("products.csv", index=False)

print("Data saved successfully to products.csv")
print(df.head())
