import requests

def get_weather(city_name):
    api_key = "84dacea845cc147376a1b963d3832215"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main_data = data["main"]
        return {
            "temperature": main_data["temp"],
            "weather": data["weather"][0]["main"]
        }
    else:
        return None

def get_song_recommendation(mood):
    api_key = "3b7df2997b4ccef20a1b2855bc81fd58"
    base_url = "http://ws.audioscrobbler.com/2.0/"
    method = "track.search"
    params = {
        "api_key": api_key,
        "method": method,
        "format": "json",
        "track": f"sad" if mood == "sad" else f"happy",
        "limit": 1
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if "trackmatches" in data:
        tracks = data["trackmatches"]["track"]
        if tracks:
            return {
                "song": tracks[0]["name"],
                "artist": tracks[0]["artist"]
            }
            print(track,'1111122222')
    return None
