from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

year = int(input("Enter Year: "))
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}-08-12/")
web = response.text
soup = BeautifulSoup(web, "html.parser")
songs = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max "
                                        "a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

song_list = []
for song in songs:
    song_list.append(song.getText().strip("\n"))

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="--your id--",
        client_secret="--your secret id--",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uri = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"Sorry {song} doesn't exist, skipped!")

playlist = sp.user_playlist_create(user=user_id, name="Billboard100-2000", public=False, collaborative=False,
                                   description='SHIT')

sp.playlist_add_items(playlist_id='5eEpcikloE8GhEmZGH9DpZ', items=song_uri)

