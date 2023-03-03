# weather_console_app(devman_api_1)

Прогноз погоды. Скрипт шлет запрос на [wttr.in/](http://wttr.in/) и печатает в консоль прогноз погоды 
из списка локаций указанных в переменной `weather_forecast_location`

Создайте виртуальное окружение
```shell
python3 -m venv /path/weather_api_console_app
```
Перейдите в папку со скриптом и активируйте виртуальное окружение.
```shell
source weather_api_console_app/bin/activate
```

Установите библиотеку Requests [руководство по установке](https://requests.readthedocs.io/en/latest/user/install/#install). Или воспользуйтесь командой ниже.
Автоматически установятся все необходимые зависимости для корректной работы библиотеки Requests.

```shell
pip install requests==2.28.2
```

Для запуска скрипта используйте команду:
```Shell
python app_main.py
````

Поддерживаемые типы местоположений:
```
    paris                  # город
    Eiffel tower           # любое местоположение
    Москва                 # юникодное имя любого местоположения на любом языке
    muc                    # код аэропорта ICAO (3 буквы)
    stackoverflow.com      # доменное имя
    94107                  # почтовый индекс (только для США)
    78.46,106.79           # GPS-координаты
```

Пример правильной работы программы:

![](https://dvmn.org/filer/canonical/1568003481/268/)



