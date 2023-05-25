import requests
from bs4 import BeautifulSoup

URL: str = 'https://www.alta.ru/currency'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
response = requests.get(URL, headers=headers)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('div', class_='module-tableSort')
rows = table.find_all('tr')
validated_rows = []

for row in rows:
    if row.find('td', 't-left') and row.find('td', 't-right'):
        new_row = row.text
        new_row = new_row.strip('\n')
        new_row = new_row.split(sep='\n')
        code = new_row[0].split(sep=' ')
        code_num = code[0]
        code_lit = code[1]
        name_rate = new_row[1]
        count_rate = new_row[2].strip(' ')
        price_rate = new_row[4]
        row_dict = {
            'Цыфровой код': code_num,
            'Буквенный код': code_lit,
            'Валюта': name_rate,
            'Кол-во едениц': count_rate,
            'Курс': price_rate
        }
        validated_rows.append(row_dict)


for item in validated_rows:
    print(item)
