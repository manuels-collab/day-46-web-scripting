import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

song_year = input("Which year do you want to travel to: Type the year in this format: YYYY-MM-DD")


header = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
response = requests.get("https://www.billboard.com/charts/hot-100/" + song_year)
soup = BeautifulSoup(response.text, "html.parser")
song_tags = soup.select("li ul li h3")
songs = [song.getText().strip() for song in song_tags]
print(songs)


client_id = "1ad5b90839f5452f900f8a73065db914"
client_secret = "bd31e5886c9f43bb856682fe7e2155c2"
user_input = input(spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="https://spotify.com").get_access_token())
