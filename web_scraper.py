from bs4 import BeautifulSoup
import requests

# Open the html file
with open("page.html", "r") as f:
    html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("ul"):
        print(tag.text)
