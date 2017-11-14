#!/usr/python3

from spotipy.oauth2 import SpotifyClientCredentials
import os, sys
import spotipy
import spotipy.util as util
import xlsxwriter

dev_username = sys.argv[1]
CBOLD = '\033[97m'
CGREEN = '\033[92m'
CRED = '\033[91m'
CEND = '\033[0m'


class Song:
	def __init__(self):
		self.data = []
		
	def request_saved_tracks():
		username = dev_username
		scope = 'user-library-read'
		token = util.prompt_for_user_token(username, scope)
		if token:
			sp = spotipy.Spotify(auth=token)
			def make_xlsx(number_of_sets):
				limit_off = 40
				off = -40
				number_of_songs = number_of_sets
				workbook = xlsxwriter.Workbook('Tracks01.xlsx')
				worksheet = workbook.add_worksheet()
				header_xlsx = ['NAME','ARTIST','URI','DANCEABILITY','ENERGY','KEY','LOUDNESS','MODE',\
							       'SPEECHINESS','ACOUSTICNESS','INSTRUMENTALNESS','LIVENESS','VALENCE',\
							       'TEMPO','DURATION_MS','ID', 'TRACK_HREF', 'ANALYSIS_URL', 'TIME SIGNATURE']
				row = 0
				col = 0
				print("[*] Building xlsx file, it might takes a few minutes")
				counter2 = 0
				for headers in header:
					worksheet.write(row, col+counter2, song_info)
					counter2 += 1
				
				for i in range(number_of_songs):
					off += 40
					results = sp.current_user_saved_tracks(limit=limit_off, offset=off)
					for item in results['items']:
						temprow = []
						track = item['track']
						song_uri = track['uri']
						song_features_list = sp.audio_features(song_uri)
						song_features = song_features_list[0]
						
						temprow.append(track['name'])
						temprow.append(track['artists'][0]['name'])
						temprow.append(song_uri)
						temprow.append(song_features['danceability'])
						temprow.append(song_features['energy'])
						temprow.append(song_features['key'])
						temprow.append(song_features['loudness'])
						temprow.append(song_features['mode'])
						temprow.append(song_features['speechiness'])
						temprow.append(song_features['acousticness'])
						temprow.append(song_features['instrumentalness'])
						temprow.append(song_features['liveness'])
						temprow.append(song_features['valence'])
						temprow.append(song_features['tempo'])
						temprow.append(song_features['id'])
						temprow.append(song_features['track_href'])
						temprow.append(song_features['analysis_url'])
						temprow.append(song_features['duration_ms'])
						temprow.append(song_features['time_signature'])
						array.append(temprow)
					for lists in array:
						if lists[0] != '':
							counter1 = 1
							for song_info in lists:
								worksheet.write(row, col+counter1, song_info)
								counter1 += 1
							row += 1
				workbook.close()
			make_xlsx(66)
			print(CGREEN + "[*] DONE!" + CEND)
		else:
			print(CRED + "Can't get token for " + sys.argv[1] + CEND)

def main():
	if len(sys.argv) < 1:
		print("You must provide a username as argument")
	else:
		Song.request_saved_tracks()

main()
