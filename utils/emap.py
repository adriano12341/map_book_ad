import requests
from bs4 import BeautifulSoup
import folium
from models.data_source import users
def single_map(user_location:str)->None:
    url: str = f'https://pl.wikipedia.org/wiki/{user_location}'
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = response_html.select(".latitude")[1].text.replace(",", ".")
    longitude = response_html.select(".longitude")[1].text.replace(",", ".")
    print(latitude)
    print(longitude)

    map = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker(location=[latitude, longitude],popup=f"{user_location} rządzi").add_to(map)
    map.save(f"./{user_location}.html")
