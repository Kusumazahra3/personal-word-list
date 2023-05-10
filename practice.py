import requests

api_key = '5da780b7-690b-4559-9bbd-61b944cafc43'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)

