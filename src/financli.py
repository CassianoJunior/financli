import argparse
import glob
import json
import os

import pandas as pd

import scraper
from lib import utils

# financli --help
# financli --version
# financli [command] --help
# financli stocks --recommended
# financli stocks --filter={ 'p/vp': { 'min': 0, 'max': 10 }, 'p/l': { 'min': 0, 'max': 10 } }
# financli stocks --filter={ 'p/vp': { 'min': 0, 'max': 10 }, 'p/l': { 'min': 0, 'max': 10 } } --sort={ 'p/vp': 'asc', 'p/l': 'desc' }
# financli stocks --filter={ 'p/vp': { 'min': 0, 'max': 10 }, 'p/l': { 'min': 0, 'max': 10 } } --sort={ 'p/vp': 'asc', 'p/l': 'desc' } --export={ 'csv': 'stocks.csv' }
# financli fiis --recommended

class Financli:
  def __init__(self):
    parser = argparse.ArgumentParser(prog='financli', description='Financli is a CLI to get financial data from B3.')
    parser.add_argument('-v, --version', action='version', version='%(prog)s 0.0.1')

    subparsers = parser.add_subparsers(title='commands', dest='command', help='Assets types available')

    parser_stocks = subparsers.add_parser('stocks', help='get stocks data')
    parser_stocks.add_argument('-r', '--recommended', help='return stocks with pre-selected filters', action='store_true')
    parser_stocks.add_argument('-f', '--filter', help='filter stocks by financial indicators', type=str)
    parser_stocks.add_argument('-s', '--sort', help='sort stocks by financial indicators', type=str)
    parser_stocks.add_argument('-e', '--export', help='export stocks to a file', type=str, default='./')
    
    parser_fiis = subparsers.add_parser('fiis', help='get fiis data')
    parser_fiis.add_argument('-r', '--recommended', help='return fiis with pre-selected filters', action='store_true')
    parser_fiis.add_argument('-f', '--filter', help='filter fiis by financial indicators', type=str)
    parser_fiis.add_argument('-s', '--sort', help='sort fiis by financial indicators', type=str)
    parser_fiis.add_argument('-e', '--export', help='export fiis to a file', type=str, default='./')

    args = parser.parse_args()

    if args.command == 'stocks':
      self.__stocks(args)
    elif args.command == 'fiis':
      self.__fiis(args)
    
  def __stocks(self, args):
    print(args)
    if args.recommended:
      print('rec')
      
    elif args.filter:
      toJson = utils.toJsonFormat(args.filter)
      print(toJson)
      toDict = json.loads(toJson)
      toDict = utils.convertNumberString(toDict)
      print(toDict)
      print(isinstance(toDict, dict))
    elif args.sort:
      print('sort')
    elif args.export:
      print('export')
    else:
      print('all')

  def __runScraperStocks(self):
    scraper.runStocks()
  
  def __runScraperFiis(self):
    scraper.runFiis()
  
  def __getLastStocks(self):
    dirname = os.path.dirname(__file__)
    rootPath = os.path.join(dirname, '..')
    pathFolder = os.path.join(rootPath, 'history', 'stocks')
    files = glob.glob(pathFolder + '/*.csv')
    files.sort(key=os.path.getmtime)

    return pd.read_csv(files[-1])
  
  def __getStocks(self):
    self.__runScraperStocks()
    return self.__getLastStocks()
  
  def __getLastFiis(self):
    dirname = os.path.dirname(__file__)
    rootPath = os.path.join(dirname, '..')
    pathFolder = os.path.join(rootPath, 'history', 'fiis')
    files = glob.glob(pathFolder + '/*.csv')
    files.sort(key=os.path.getmtime)

    return pd.read_csv(files[-1])
  
  def __getFiis(self):
    self.__runScraperFiis()
    return self.__getLastFiis()
  

