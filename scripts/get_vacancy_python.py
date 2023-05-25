import requests
from random import randint, sample

def get_random_vacancy():
    # определяем URL с вакансиями
    URL: str = 'https://api.hh.ru/vacancies?'

    # создаем заголовки, в которых нашем агентом будет не браузер, а тест апи (так требует hh.ru)
    headers: dict = {
        'User-Agent': 'api-test-agent'
    }
    # определяем словарь с параметрами запроса, чтобы не передавать все в строке так:
    # https://api.hh.ru/vacancies?page=1&per_page=100&text=python&area=2
    params: dict = {
        'page': '1',        # страница
        'per_page': '100',  # количество результатов на странице
        'text': 'python',   # встречается в тексте
        'area': '2'         # область Санкт-Петербург
    }

    ids: list = [str]   #список для id вакансий
    resp = requests.get(URL, headers=headers, params=params)
    data = resp.json()
    count_page = data['pages']  # количество страниц с результатами
    count_id = data['found']    # всего вакансий найдено

    # проходимся по каждой странице
    for i in range(count_page + 1):
        resp = requests.get(f'https://api.hh.ru/vacancies?page={i}&per_page=100&text=python&area=2')
        data = resp.json()
        # и получаем с нее все id вакансий
        for item in data['items']:
            ids.append(item['id'])
    print(f'found ids = {count_id}, parsed ids = {len(ids)}')

    # получаем три случайных значения из списка id вакансий
    rand_ids = sample(ids, 3)
    list_of_data_vacancy: list = [dict]

    # заходим на страничку каждой вакансии и заносим нужные нам поля в словарь
    for id in rand_ids:
        #URL с API, выдающем информацию по конкретной вакансии
        url_rand_vacancies = f'https://api.hh.ru/vacancies/{id}'
        resp_vacancies = requests.get(url=url_rand_vacancies, headers=headers).json()
        data_vacancy = {'name': resp_vacancies["name"],
                        'created_at': resp_vacancies["created_at"],
                        'salary': resp_vacancies["salary"],
                        'url': resp_vacancies["alternate_url"]
                        }
        # каждый из словарей заносим в список
        # заносим именно копию словаря, так как в листе будут ссылки на словарь, а не сам словарь
        # и если заносить не копию, то все три раза будет меняться один и тот же словарь
        list_of_data_vacancy.append(data_vacancy.copy())


    return list_of_data_vacancy

if __name__ == '__main__':
    get_random_vacancy()