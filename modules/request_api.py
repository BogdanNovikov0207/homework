import requests
# импортирует модуль для запросов на сервер
from .read_json import read_json
# импортирует функцию для чтения json файлов
import json
# импортирует сам json для работы с python
data_api = read_json(name_file= 'config_api.json')
# переменная которая хранит в себе данные из конфига апи
API_KEY = data_api['api_key']
# константа в которой мы используем нужные данные, сохраненные в переменную data_api
CITY_NAME = data_api['city_name']
# константа в которой мы используем нужные данные, сохраненные в переменную data_api
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# константа, в которой содержится ссылка. Мы передаем туда название города, погода которого нам интересна и используем наш апи ключ для авторизации на сервере
response = requests.get(URL)
# получает данные с сервера, используя информацию которая находится в URL
if response.status_code == 200:
    # если данные были получены, то:
    data_dict = json.loads(response.content)
    # превращает байт код, который мы получили с сервера в словарь
    print(json.dumps(data_dict, indent= 4))