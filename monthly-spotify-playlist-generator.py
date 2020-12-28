import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_season(month):
    if month in ("01","11","12"):
        return " Winter ", "❄"
    elif month in ("02","03","04"):
        return " Spring ", "🌸"
    elif month in ("05", "06", "07"):
        return " Summer ", "🌞"
    else:
        return " Autumn ", "🍂"

def add_to_specific_month_playlist(year, month, track):
    season = get_season(month)
    playlist_name = season[1] + season[0] + year + " " + season[1]
    playlist_exists = False
    playlist_id = ""
    user_playlists = sp.current_user_playlists()

    for item in user_playlists["items"]:
        if playlist_name == item['name']:
            playlist_id = item["id"]
            playlist_exists = True

    if playlist_exists is False:
        newly_created_playlist = sp.user_playlist_create(os.environ["USER_ID"], playlist_name, description= "Automatically generated playlist for" + season[0] + year + season[1] + "            https://github.com/neasatang/monthly-spotify-playlist-generator" )
        playlist_id = newly_created_playlist["id"]

    sp.playlist_add_items(playlist_id, {track})


scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_user_playlists()

playlist = sp.playlist(os.environ["PLAYLIST_ID"])
total = playlist["tracks"]["total"]
offset = 0

while offset != total:
    playlist_tracks = sp.playlist_items(os.environ["PLAYLIST_ID"], offset=offset)
    for item in playlist_tracks["items"]:
        date = item["added_at"].split("-")
        if item["track"] is not None:
            track_id = item["track"]["id"]
            if track_id is not None:
                add_to_specific_month_playlist(date[0], date[1], track_id)
                new_track_id = sp.track(track_id)
        offset += 1
