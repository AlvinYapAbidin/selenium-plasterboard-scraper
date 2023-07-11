import requests
from bs4 import BeautifulSoup

PLASTERBOARD_URL = "https://www.blacktownbuildingsupplies.com.au/product-category/building-supplies/plasterboard-accessories/plasterboard/"
cert_path = "ZscalerRoot.pem"

response = requests.get(PLASTERBOARD_URL, verify=cert_path)

print('Status Cost', response.status_code)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title', doc.title.text)

# Find all the item divs
item_divs = doc.find_all('div', class_="supp_cl")

print(f'Found {len(item_divs)} items')
