# monthly-spotify-playlist-generator

Generates seasonal playlists that you may want to create from a big playlist that you have over the years
<img src="image.png" width="=20">


## Setup 
Some environment variables required to run the script:
| Key                   | Val                            | 
| --------------------- | ------------------------------:|
| SPOTIPY_CLIENT_ID     | spotify client ID              |
| SPOTIPY_CLIENT_SECRET | spotify client secret          |
| SPOTIPY_REDIRECT_URI  | spotify redirect uri           |
| PLAYLIST_ID           | big playlist that you have     |
| USER_ID               | user id that owns the playlist |


## Different scripts
* most-recent-montly-spotify-playlist-generator.py 
    * generates the playlist for the last season
* montly-spotify-playlist-generator.py 
    * generates the playlist for all the past seasons
    
    
## Bugfix:
* Need to change the `most-recent-montly-spotify-playlist-generator.py` so that it gets the current season rather than month/year (generating it on a monthly basis was the initial idea but i changed to using seasons instead and forgot to change it during implementation) 
* Need to rename files to use the word `seasonal` instead of `monthly`
