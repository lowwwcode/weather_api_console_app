import requests


def get_weather_forecast(loc):
    """Функция, которая возвращает прогноз погоды если передать ей локацию"""
    url_template = 'http://wttr.in/{}'
    ready_url = url_template.format(loc)
    params = {'mMnqT': '', 'lang': 'ru'}
    response = requests.get(ready_url, params=params)
    response.raise_for_status()
    return response.text.strip()


if __name__ == '__main__':
    weather_forecast_locations = ['Лондон', 'Шереметьево', 'Череповец']
    for location in weather_forecast_locations:
        print(get_weather_forecast(location))