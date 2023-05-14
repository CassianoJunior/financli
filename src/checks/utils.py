
def checkInterval(interval: dict):
  availableIntervalOptions = ['min', 'max']

  intervals = interval.keys()

  for i in intervals:
    if i not in availableIntervalOptions:
      return {
        'status': False,
        'reason': f'Interval {i} is not available'
      }
    
    result = checkType(interval[i], [int, float])

    if not result: 
      return {
        'status': False,
        'reason': f'Interval {i} is not a float or integer'
      }
    
    return {
      'status': True
    }

def checkType(value, types):
  for t in types:
    if not type(value) == t: return False
  
  return True

def checkSortType(sort: str): 
  availableSortOptions = ['asc', 'desc']

  if sort not in availableSortOptions:
    return {
      'status': False,
      'reason': f'Sort {sort} is not available'
    }
  
  return {
    'status': True
  }
