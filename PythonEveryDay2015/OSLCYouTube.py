# Print stats on the Oslc playlist 
# From http://pythonhosted.org/pafy/
# Typer and developer: Ginny C Ghezzo 
# What I learned: This is useful : https://raw.githubusercontent.com/np1/pafy/master/pafy/pafy.py
# Todo: The import is too slow 

import pafy
import time 
oslc_url = "https://www.youtube.com/watch?v=QDEu3xoazoI&list=PL8968B48E8DD75B34"

playlist = pafy.get_playlist(oslc_url)
print("Title =", playlist['title'])
print("Number of Videos =", len(playlist['items']))
count = 0
for pf in playlist['items']:
	count = count +1 
	video = pf['pafy']
	print(count, video.title)
	print('  Rating & Likes: {} & {} '.format(video.rating, video.likes))
	# print('  Author = ', video.author)
	print('  Views: ',video.viewcount)
	minute, second = divmod(video.length,60)
	print('  Length: {}:{}'.format(minute, second))
