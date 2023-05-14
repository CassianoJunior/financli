# Cotação,P/L,P/VP,PSR,Div.Yield,P/Ativo,P/Cap.Giro,P/EBIT,P/Ativ.Circ.Liq,EV/EBIT,EV/EBITDA,Mrg Ebit,
# Mrg. Líq.,Liq. Corr.,ROIC,ROE,Liq.2meses,Patrim. Líq,Dív.Brut/ Patrim.,Cresc. Rec.5a,
from utils import checkInterval, checkSortType, checkType


def checkFilter(filter: dict):
  availableFilterOptions = [
    'cot',        # Quotation: interval float,int
    'p/l',        # Price/earnings: interval float,int
    'p/vp',       # Price/asset value: interval float,int
    'psr',        # Price/sales: interval float,int
    'yield',      # Dividend Yield: interval float,int
    'p/at',       # Price/asset: interval float,int
    'p/cg',       # Price/capital rotation: interval float,int
    'p/ebit',     # Price/ebit: interval float,int
    'p/ativcirc', # Price/circulating assets: interval float,int
    'ev/ebit',    # Enterprise value/ebit: interval float,int
    'ev/ebitda',  # Enterprise value/ebitda: interval float,int
    'mrgEbit',    # Ebit margin: interval float,int
    'mrgLiq',     # Net margin: interval float,int
    'liqCorr',    # Current liquidity: interval float,int
    'roic',       # Return on invested capital: interval float,int
    'roe',        # Return on equity: interval float,int
    'liq2m',      # 2 months liquidity: interval float,int
    'pliq',       # Net patrimony: interval float,int
    'div/p',      # Gross debt/net patrimony: interval float,int
    'cresc'       # 5 years revenue growth: interval float,int
  ]

  filters = filter.keys()

  for f in filters:
    if f not in availableFilterOptions:
      return {
        'status': False,
        'reason': f'Filter {f} is not available'
      }

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
    'cot',        # Quotation: [asc, desc]
    'p/l',        # Price/earnings: [asc, desc]
    'p/vp',       # Price/asset value: [asc, desc]
    'psr',        # Price/sales: [asc, desc]
    'yield',      # Dividend Yield: [asc, desc]
    'p/at',       # Price/asset: [asc, desc]
    'p/cg',       # Price/capital rotation: [asc, desc]
    'p/ebit',     # Price/ebit: [asc, desc]
    'p/ativcirc', # Price/circulating assets: [asc, desc]
    'ev/ebit',    # Enterprise value/ebit: [asc, desc]
    'ev/ebitda',  # Enterprise value/ebitda: [asc, desc]
    'mrgEbit',    # Ebit margin: [asc, desc]
    'mrgLiq',     # Net margin: [asc, desc]
    'liqCorr',    # Current liquidity: [asc, desc]
    'roic',       # Return on invested capital: [asc, desc]
    'roe',        # Return on equity: [asc, desc]
    'liq2m',      # 2 months liquidity: [asc, desc]
    'pliq',       # Net patrimony: [asc, desc]
    'div/p',      # Gross debt/net patrimony: [asc, desc]
    'cresc'       # 5 years revenue growth: [asc, desc]
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