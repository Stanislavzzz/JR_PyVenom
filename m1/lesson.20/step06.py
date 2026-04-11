import requests


# print(requests.__version__)

url = "https://nalog.ru"

response = requests.get(url)

print(response)
print(f"Статус код: {response.status_code}")
print(f"Заголовки: {response.headers}")
print(f"Тело ответа: {response.text}")
