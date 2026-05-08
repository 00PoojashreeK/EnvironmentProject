import requests

def get_weather(city):
    api = "061348bfaf176f34f13c1f57d019821b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

    try:
        res = requests.get(url).json()
        return res["main"]["temp"], res["weather"][0]["description"]
    except:
        return None, None