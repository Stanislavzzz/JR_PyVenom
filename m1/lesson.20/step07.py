import requests


# print(requests.__version__)
lang = 'ru'
prog = 'python'

url = f"https://ya.ru/search/?text={prog}&lang={lang}"

response = requests.get(url)

print(response)
print(f"Статус код: {response.status_code}")
print(f"Заголовки: {response.headers}")
print(f"Тело ответа: {response.text}")
