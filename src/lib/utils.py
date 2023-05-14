import re


# {foo: bar} -> {"foo": "bar"} || {foo: 1, bar: {foo: bar}} -> {"foo": 1, "bar": {"foo": "bar"}}
def toJsonFormat(text):
  dictCount = re.findall(r'{', text)
  dictCount = len(dictCount)

  for i in range(dictCount):
    text = re.sub(r'([a-zA-Z0-9_]+)(:)', r'"\1"\2', text)
    text = re.sub(r'(:)([a-zA-Z0-9_]+)', r'\1"\2"', text)
    text = re.sub(r'([a-zA-Z0-9_]+)(,)', r'"\1"\2', text)

  return text.replace(',}', '}')

def convertNumberString(dictionary):
  for key in dictionary.keys():
    if isinstance(dictionary[key], dict):
      dictionary[key] = convertNumberString(dictionary[key])
      continue

    if dictionary[key].isdigit():
      dictionary[key] = int(dictionary[key])
    elif dictionary[key].replace('.', '', 1).isdigit():
      dictionary[key] = float(dictionary[key])
  return dictionary
