import spotipy
import spotipy.util as util
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Define gsheets scope
gsheets_scope = ['https://spreadsheets.google.com/feeds']
# Import credits for google sheets
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', gsheets_scope)
# Authenticate client
client = gspread.authorize(creds)
# Grab first sheet of music data
music_data = client.open('Music v4.5.2').sheet1
# Define spotify scope
spotify_scope = 'user-top-read playlist-read-private playlist-modify-private playlist-read-collaborative'
# Define username
username = 'Sebastien0302'
# Define client id
client_id =''
# Define client secret
client_secret = ''
# Define redirect url
redirect_url = 'http://localhost/'

# Get spotify authorization token
token = util.prompt_for_user_token(username, spotify_scope, client_id, client_secret, redirect_url)
# Authentication success
if token:
	# Define api object
	api = spotipy.Spotify(auth=token)
	# Status update
	print('Start', api.user_playlist('Sebastien0302', '45A81UhV56xPwiQga6eQ94')['tracks']['total'])
	# Grab all spotify IDs
	track_ids = music_data.col_values(6)[1:-2]
	# Add in batches of 100 from spreadsheet
	api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', track_ids[:100])
	api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', track_ids[100:200])
	api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', track_ids[200:300])
	api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', track_ids[300:400])
	api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', track_ids[400:500])
	api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', track_ids[500:])
	# Status update
	print('Spreadsheet imported', api.user_playlist('Sebastien0302', '45A81UhV56xPwiQga6eQ94')['tracks']['total'])
	# List of my playlists
	my_playlists = api.user_playlists(username)
	# For all playlists
	for playlist in my_playlists['items']:
		# If "All" playlist
		if(playlist['id'] == '45A81UhV56xPwiQga6eQ94'):
			# Skip
			continue
		# Current song number in parsing through the playlist "All"
		track_number = 0
		# List of all songs
		all_tracks =[]
		# The next batch of songs from "All"
		next_hundred = api.user_playlist_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', None, 100, track_number)['items']
		# While there are more songs
		while(len(next_hundred) > 0):
			# Add the next batch to the list
			all_tracks += next_hundred
			# Incremeent the song counter
			track_number += 100
			# Load the next batch of songs
			next_hundred = api.user_playlist_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', None, 100, track_number)['items']
		# Grab just track data
		all_tracks = [track['track'] for track in all_tracks]
		# Get the tracks of the playlist
		current_tracks = api.user_playlist_tracks(playlist['owner']['id'], playlist['id'], None, 100, 0)['items'] + api.user_playlist_tracks(playlist['owner']['id'], playlist['id'], None, 100, 100)['items']
		# New songs from this playlist
		new_tracks = [track['track']['id'] for track in current_tracks if track['track'] not in all_tracks]
		if(len(new_tracks) == 0):
			# Status update
			print(playlist['name'], 'imported', api.user_playlist('Sebastien0302', '45A81UhV56xPwiQga6eQ94')['tracks']['total'])
			continue
		if(len(new_tracks) > 100):
			api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', new_tracks[:100])
			api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', new_tracks[100:])
		else:
			api.user_playlist_add_tracks('Sebastien0302', '45A81UhV56xPwiQga6eQ94', new_tracks)
		# Status update
		print(playlist['name'], 'imported', api.user_playlist('Sebastien0302', '45A81UhV56xPwiQga6eQ94')['tracks']['total'])
# Authentication failure
else:
	# Notify user
	print("Can't get token for", username)