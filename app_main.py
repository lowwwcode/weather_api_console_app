import requests

weather_forecast_location = 'Череповец'
url_template = 'https://wttr.in/{}?mnTqu&lang=ru'
ready_url = url_template.format(weather_forecast_location)
response = requests.get(ready_url)
response.raise_for_status()

print(response.text.strip())
