import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("City? ")

params = {
    'q': city,
    'units': 'metric',
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7'
}

res = requests.get(api_url, params=params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json()) # returns json.loads(res.text)

data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))























