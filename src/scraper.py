import os
from datetime import datetime as dt

import pandas as pd
import requests
from bs4 import BeautifulSoup


def runStocks():
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
  df['description'] = pd.DataFrame(stockDescription)['description']

  # Exporting the dataframe to a csv file
  dirname = os.path.dirname(__file__)
  rootPath = os.path.join(dirname, '..')
  pathFolder = os.path.join(rootPath, 'history', 'stocks')
  if not os.path.exists(pathFolder): os.makedirs(pathFolder)

  date = dt.today().strftime("%d-%m-%Y_%H-%M-%S")

  df.to_csv(os.path.join(pathFolder, f'stocks-{date}.csv'), index=False)

def runFiis():
  # URL to be scraped
  url = 'https://www.fundamentus.com.br/fii_resultado.php?&interface=classic'

  # Requesting the page
  page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

  # Parsing the page
  soup = BeautifulSoup(page.text, 'html.parser')

  # Getting the table header
  table_header = soup.find('table', {'id': 'tabelaResultado'}).find('thead').find('tr').find_all('th')
  tableHeaders = [th.get_text().strip() for th in table_header]

  # Getting the table data
  table_data = soup.find('table', {'id': 'tabelaResultado'}).find('tbody').find_all('tr')

  tableData = []
  for tr in table_data:
    cols = tr.find_all('td')
    tableData.append([td.get_text().strip() for td in cols])

  # Creating the dataframe
  df = pd.DataFrame(tableData, columns=tableHeaders)

  # Exporting the dataframe to a csv file
  dirname = os.path.dirname(__file__)
  rootPath = os.path.join(dirname, '..')
  pathFolder = os.path.join(rootPath, 'history', 'fiis')
  if not os.path.exists(pathFolder): os.makedirs(pathFolder)

  date = dt.today().strftime("%d-%m-%Y_%H-%M-%S")

  df.to_csv(os.path.join(pathFolder, f'fiis-{date}.csv'), index=False)