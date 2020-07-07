from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

# we use the find method to search HTML elements. The first params is the element tag and the second is a dictionary
# OBJ with the attr and value
results = soup.find("ol", {"id", "b_results"})

# We create a links variable that stores all the li
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    # We get the anchor tag text
    item_text = item.find("a").text
    # We get the URL
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)