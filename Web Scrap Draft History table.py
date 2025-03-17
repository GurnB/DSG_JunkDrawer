#
# Webs Scraping test on the StatsPlus.net Draft History web page



import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://statsplus.net/americanbaseballlegion/draftyear/?year=2018"

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
    
table = soup.find("table")

if table is None:
    print("Table not found.")
    exit()

for row in table.find_all("tr"):
    headers = row.find_all("th")
    if headers:
        header_data = [header.text.strip() for header in headers]
        print(header_data)
    cells = row.find_all("td")
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        print(row_data)