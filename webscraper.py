import requests

PLASTERBOARD_URL = "https://www.blacktownbuildingsupplies.com.au/product/"

response = requests.get(PLASTERBOARD_URL)

print('Status Cost', response.status_code)