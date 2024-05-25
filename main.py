import requests

url = "https://books.toscrape.com"

proxies = {
    "http": "185.244.210.185:80"
    }

try:
    page = requests.get(url, proxies=proxies)
    print(page.content)
except requests.exceptions.ProxyError as e:
    print(f"Proxy error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
