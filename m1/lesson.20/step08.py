import requests


lang = 'ru'
prog = 'python'

url = "https://ya.ru/search/"

params = {
    'text': prog,
    'lang': lang
}

response = requests.get(url, params=params)

print(response)
print(f"Статус код: {response.status_code}")
print(f"Заголовки: {response.headers}")
print(f"Тело ответа: {response.text}")
