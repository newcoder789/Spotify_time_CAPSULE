song_year = int(input("which year do you want to travel to in YYYY(from 1960 to 2020):\n"))


from bs4 import BeautifulSoup
import requests

from indian_song_list import songs
from spotify_tests import Spotify_tasks

s = Spotify_tasks()

if song_year < 1960 or song_year > 2022:
    print("Sorry we dont have data for your asked list")
elif song_year < 1970:
    s.create_playlist(songs[1960], "1960s")
elif song_year >= 2010:
    s.create_playlist(songs[song_year], song_year)
elif song_year < 1980:
    url_1970 = "https://www.jiosaavn.com/featured/hindi-1970s/Pgp0Amd0LZnuCJW60TJk1Q__"
    response = requests.get(url=url_1970)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = soup.select("ol li h4 a")
    songs_list = []
    for i in song_names:
        songs_list.append(i.get_text())
    print(songs_list)
    s.create_playlist(songs_list, "1970s")
elif song_year < 1990:
    url_1980 = "https://www.jiosaavn.com/featured/hindi-1980s/,H6xc4W4ZikV3Xpvr9dnYw__"
    response = requests.get(url=url_1980)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = soup.select("ol li h4 a")
    songs_list = []
    for i in song_names:
        songs_list.append(i.get_text())
    print(songs_list)
    s.create_playlist(songs_list, "1980s")
elif song_year < 2000:
    url_1990 = "https://www.jiosaavn.com/featured/hindi-1990s/dSYq41esdPJAI5VmDfZSSg__"
    response = requests.get(url=url_1990)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = soup.select("ol li h4 a")
    songs_list = []
    for i in song_names:
        songs_list.append(i.get_text())
    print(songs_list)
    s.create_playlist(songs_list, "1990s")
elif song_year < 2010:
    url_2000 = "https://www.jiosaavn.com/featured/hindi-2000s/dSYq41esdPJwtkLw7-JlUw__"
    response = requests.get(url=url_2000)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = soup.select("ol li h4 a")
    songs_list = []
    for i in song_names:
        songs_list.append(i.get_text())
    print(songs_list)
    s.create_playlist(songs_list, "2000s")
else:
    print("shutup")

