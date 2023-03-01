import requests


def get_weather_forecast(loc):
    """Функция, которая возвращает прогноз погоды если передать ей локацию"""
    url_template = 'https://wttr.in/{}?mnTqu&lang=ru'
    ready_url = url_template.format(loc)
    response = requests.get(ready_url)
    response.raise_for_status()
    return response.text.strip()


weather_forecast_locations = ['Лондон', 'Шереметьево', 'Череповец']
for location in weather_forecast_locations:
    print(get_weather_forecast(location))
