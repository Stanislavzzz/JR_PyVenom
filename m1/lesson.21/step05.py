import requests


url = "https://httpbin.org/status/404"

# data = {
#     'user_name': 'Bob',
#     'user_age': 32,
#     'password': '1234567890',
# }

response = requests.get(url)

print(response)
print("*" * 50)
print(f"Статус код: {response.status_code}")
print("*" * 50)
print(f"Статус код: {response.raise_for_status()}")
print("*" * 50)
print(f"Тело ответа: {response.text}")
