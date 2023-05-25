import requests                         # библиотека HTTP-запросов
from bs4 import BeautifulSoup           # библиотека для парсинга html-страницы
from fake_useragent import UserAgent    # класс для user-agent

# определяем функцию получения погоды. -> list говорит о том, что результатом будет список
def get_weather_spb() -> list:
    # создаем объект класса UserAgent для генерации случайного значения браузера
    ua = UserAgent()
    # наш сайт с погодой
    URL: str = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
    # выполняем GET-запрос к сайту
    response = requests.get(URL, headers={'User-agent': ua.random})
    # получаем html-код страницы из ответа
    html: str = response.text
    # создаем объект класса BeautifulSoup. 1-й аргумент - код html-страницы, 2-й аргумент - парсер для html ('html.parser')
    soup = BeautifulSoup(html, 'html.parser')
    # получаем дату со странички по тегу: <div class="dates short-d"><span>Среда</span>, 19 апреля</div>
    date: str = soup.find('div', 'dates short-d').text
    # получаем таблицу по тегу: <table class="weather-today short">
    table_weather_today = soup.find('table', 'weather-today short')
    # находим все строки <tr> в найденной таблице
    rows_table_today = table_weather_today.find_all(name='tr')
    # создаем список, куда будем вносить погоду по времени суток за день (ночь, утро, день, вечер)
    weather_day_list: list = []

    # в каждой строке таблицы ищем столбец с нужным названием и заносим в словарь
    for row in rows_table_today:
        # для каждого времени суток создаем свой словарь
        info_weather: dict = {}
        info_weather['weather_day'] = row.find('td', 'weather-day').text
        info_weather['temperature'] = row.find('td', 'weather-temperature').text
        info_weather['tooltip'] = row.find('div')['title']
        info_weather['weather-feeling'] = row.find('td', 'weather-feeling').text
        info_weather['weather-humidity'] = row.find('td', 'weather-humidity').text
        # заносим текущий словарь в список
        weather_day_list.append(info_weather)

    # в начало списка заносим дату
    weather_day_list.insert(0, date)

    # возвращаем из функции список
    return weather_day_list


if __name__ == '__main__':
    print(*get_weather_spb(), sep='\n')


