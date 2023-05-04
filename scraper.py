import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = 'https://www.fundamentus.com.br/resultado.php?&interface=classic'

# Requesting the page
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# Parsing the page
soup = BeautifulSoup(page.text, 'html.parser')

# Getting the table header
table_header = soup.find('table', {'id': 'resultado'}).find('thead').find('tr').find_all('th')
tableHeaders = [th.get_text().strip() for th in table_header]

# Getting the table data
table_data = soup.find('table', {'id': 'resultado'}).find('tbody').find_all('tr')

stockDescription = []
tableData = []
for tr in table_data:
  cols = tr.find_all('td')
  description = cols[0].find('span').get('title')
  stockDescription.append({'description': description, 'stock': cols[0].get_text().strip()})
  tableData.append([td.get_text().strip() for td in cols])


# Creating the dataframe
df = pd.DataFrame(tableData, columns=tableHeaders)

# Adding the stock description
df['stockDescription'] = pd.DataFrame(stockDescription)['description']

# Exporting the dataframe to a csv file
df.to_csv('stocks.csv', index=False)


