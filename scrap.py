import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

proxies = {
    "http": "185.244.210.185:80",
    "http": "49.13.161.231:80",
    "http": "72.10.164.178:5657",
    "http": "147.251.6.31:3128",
    "http": "72.10.160.174:4881",
    "http": "67.43.227.227:20627",
    "http": "72.10.160.90:32073",
    }

# Fetch the page content
try:
    response = requests.get(url, proxies=proxies)  # Add proxies=proxies if needed
    response.raise_for_status()  # Check if the request was successful
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
else:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract book titles
    books = soup.find_all('h3')
    for book in books:
        title = book.find('a')['title']
        print(title)
