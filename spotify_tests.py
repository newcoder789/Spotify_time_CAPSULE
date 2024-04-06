# url = "https://example.org/callback"
#
#
# # -----------------this code to log in to the spotify
#
from pprint import pprint

Client_ID = YOUR Client_ID
Client_Secret = YOUR CLIENT Client_Secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
    )
)
user_id = sp.current_user()["id"]

class Spotify_tasks:
    def __init__(self):
        self.song_uris = []

    def create_playlist(self, final_song_list, song_year):
        for song in final_song_list:
            result = sp.search(song)['tracks']['items'][0]['uri']
            try:
                self.song_uris.append(result)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        print(self.song_uris)
        playlist = sp.user_playlist_create(user=user_id, name=f"{song_year} Time_Capsule", public=False)
        print(playlist)


        sp.playlist_add_items(playlist_id=playlist["id"], items=self.song_uris)
