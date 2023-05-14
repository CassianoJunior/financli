# Segmento,Cotação,FFO Yield,Dividend Yield,P/VP,Valor de Mercado,Liquidez,Qtd de imóveis,Preço do m2,Aluguel por m2,Cap Rate,Vacância Média
from utils import checkInterval, checkSortType, checkType


def checkFilter(filter: dict):
  availableFilterOptions = [
    'seg',       # Segment: str
    'cot',       # Quotation: interval float,int
    'yield',     # Dividend Yield: interval float,int
    'ffoYield',  # FFO Yield: interval float,int
    'p/vp',      # Price/asset value: interval float,int
    'mktVal',    # Market value: interval float,int
    'liq',       # Liquidity: interval float,int
    'propCount', # Property count: interval float,int
    'pricem2',   # Price per square meter: interval float,int
    'rentm2',    # Rent per square meter: interval float,int
    'capRate',   # Capitalization rate: interval float,int
    'vacAvg'     # Average vacancy: interval float,int
  ]

  filters = filter.keys()

  for f in filters:
    if f not in availableFilterOptions:
      return {
        'status': False,
        'reason': f'Filter {f} is not available'
      }
    
    if f == 'seg':
      result = checkType(filter[f], [str])
      
      if not result:
        return {
          'status': False,
          'reason': f'Filter {f} is not a string'
        }
      
      availableSegmentOptions = [
        'hosp',  # Hospital
        'hotel', # Hotel
        'hib',   # Hybrid
        'lage',  # Lage
        'log',   # Logistic
        'other', # Other
        'resid', # Residential
        'shop',  # Shopping
        'titles', # Marketable securities
      ]

      if filter[f] not in availableSegmentOptions:
        return {
          'status': False,
          'reason': f'Segment {filter[f]} is not available'
        }
      
      continue

    result = checkInterval(filters[f])

    if not result['status']:
      return {
        'status': False,
        'reason': result['reason'] + f' in filter {f}'
      }

  return {
    'status': True
  }

def checkSort(sort: dict):
  availableSortOptions = [
    'seg',       # Segment: [asc, desc]
    'cot',       # Quotation: [asc, desc]
    'yield',     # Dividend Yield: [asc, desc]
    'ffoYield',  # FFO Yield: [asc, desc]
    'p/vp',      # Price/asset value: [asc, desc]
    'mktVal',    # Market value: [asc, desc]
    'liq',       # Liquidity: [asc, desc]
    'propCount', # Property count: [asc, desc]
    'pricem2',   # Price per square meter: [asc, desc]
    'rentm2',    # Rent per square meter: [asc, desc]
    'capRate',   # Capitalization rate: [asc, desc]
    'vacAvg'     # Average vacancy: [asc, desc]
  ]

  sorts = sort.keys()

  for s in sorts:
    if s not in availableSortOptions:
      return {
        'status': False,
        'reason': f'Sort {s} is not available'
      }

    result = checkType(sort[s], [str])

    if not result:
      return {
        'status': False,
        'reason': f'Sort {s} is not a string'
      }

    result = checkSortType(sort[s])

    if not result['status']:
      return {
        'status': False,
        'reason': result['reason'] + f' in sort {s}'
      }
  
  return {
    'status': True
  }