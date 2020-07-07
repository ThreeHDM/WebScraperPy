#   We import BeautifulSoup
from bs4 import BeautifulSoup
#   We import requests
import requests

#   We build the URL and send a GET request. Then we store the response (r)
search = input("Enter search term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

#   We pass the response text to the BS object
soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())


