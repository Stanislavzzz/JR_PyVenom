import requests


def get_weather(our_city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    api_key = "eddca6f589afb240832059499594ed8b"
    city = our_city

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json().get("main").get('temp')
        print(f'get_weathe - {__name__=}')
        return data


if __name__ == '__main__':
    weather = get_weather('Владивосток')
    print(weather)

    print(__name__)