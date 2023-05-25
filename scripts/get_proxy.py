import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

class Response:
    URL = 'https://spys.one/'
    USER_AGENT = UserAgent().random
    HEADERS = {"User-Agent": USER_AGENT}

    @classmethod
    def get_soup(self):
        resp = requests.get(self.URL, headers=self.HEADERS)
        soup = BeautifulSoup(resp.text, 'html.parser')

        return soup

class Proxy:

    def __init__(self, soup) -> None:
        self.soup: BeautifulSoup = soup

    def get_proxy(self):
        table_proxy = self.soup.find_all('table')[3]
        rows_proxy = table_proxy.find_all('tr', ['spy1xx', 'spy1x'])
        headers_proxy = [i.text for i in rows_proxy[0]]
        proxy_list = []

        for row in rows_proxy[1:]:
            proxy_dict = {}.fromkeys(headers_proxy)
            td_list = row.find_all('td')
            for i in range(len(td_list)):
                proxy_dict[headers_proxy[i]] = td_list[i].text

            proxy_list.append(proxy_dict)

        return proxy_list



soup = Response.get_soup()
proxy = Proxy(soup)
proxy_list = proxy.get_proxy()
pass