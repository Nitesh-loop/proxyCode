# Import the required Modules 
import requests 

# Create a pool of proxies 
proxies = {
    "http": "185.244.210.185:80",
    "http": "49.13.161.231:80",
    "http": "72.10.164.178:5657",
    "http": "147.251.6.31:3128",
    "http": "72.10.160.174:4881",
    "http": "67.43.227.227:20627",
    "http": "72.10.160.90:32073",
    } 

url = 'https://ipecho.net/plain'

# Iterate the proxies and check if it is working. 
for proxy in proxies: 
	try: 

		# https://ipecho.net/plain returns the ip address 
		# of the current session if a GET request is sent. 
		page = requests.get(url, proxies=proxies) 

		# Prints Proxy server IP address if proxy is alive. 
		print("Status OK, Output:", page.text) 

	except OSError as e: 

		# Proxy returns Connection error 
		print(e) 
