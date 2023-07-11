import requests
from bs4 import BeautifulSoup

PLASTERBOARD_URL = "https://www.youtube.com/feed/trending"
cert_path = "ZscalerRoot.pem"

response = requests.get(PLASTERBOARD_URL, verify=cert_path)

print('Status Cost', response.status_code)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title', doc.title.text)

# Find all the item divs
item_divs = doc.find_all('div', class_="ytd-video-renderer")

print(f'Found {len(item_divs)} items')