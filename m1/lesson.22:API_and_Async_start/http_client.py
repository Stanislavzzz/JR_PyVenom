import requests


url = 'http://127.0.0.1:8080/about/'

data = {
    "name": "Bob",
    "email": "Bob@mail.ru",
    "age": 32,
}

# response = requests.get(url)
response = requests.post(url, data=data)

print(response.status_code)
print(response.text)