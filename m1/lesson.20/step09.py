import requests


url = "https://httpbin.org/headers"

headers = {
    'User-Agent': 'JavaRush',
    'Token_JR': '123QWERTY'
}

response = requests.get(url, headers=headers)

print(response)
print(f"Статус код: {response.status_code}")
print(f"Заголовки: {response.headers}")
print(f"Тело ответа: {response.text}")
