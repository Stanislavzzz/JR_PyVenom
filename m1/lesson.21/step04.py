import requests


url = "https://httpbin.org/post"

data = {
    'user_name': 'Bob',
    'user_age': 32,
    'password': '1234567890',
}

response = requests.post(url, data=data)
# response = requests.post(url, json=json)

print(response)
print(f"Статус код: {response.status_code}")
print(f"Заголовки: {response.headers}")
print(f"Тело ответа: {response.text}")
