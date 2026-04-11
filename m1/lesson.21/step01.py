import requests


url = "https://httpbin.org/get"

headers = {
    'User-Agent': 'JavaRush',
    'Token_JR': '123QWERTY'
}

data = {
    'user': 'Bob',
    'password': '1234567890'
}
# response = requests.get(url, headers=headers)
response = requests.post(url, data=data)
# response = requests.put(url, data=data)
# response = requests.delete(url)

print(response)
print(f"Статус код: {response.status_code}")
print(f"Заголовки: {response.headers}")
print(f"Тело ответа: {response.text}")
