# Try to use google api 
# Developer: Ginny C Ghezzo 
# References:  http://wescpy.blogspot.com/2014/11/authorized-google-api-access-from-python.html

import apiclient.discovery		# No idea : http://wescpy.blogspot.com/2014/09/simple-google-api-access-from-python.html
from apiclient.discovery import build 
import sys

SERVERKEY = input("Shhh What is your API Blogger Server Key (hint AIz) : ")
SEARCHSTRING = input("What do you want to search google plus for? ")
if SEARCHSTRING == '': 
	SEARCHSTRING = 'python'

print(SERVERKEY)
gplus = build('plus', 'v1', developerKey=SERVERKEY)	# produces a discover.Resouce.object
# search(), which lets you query public activities
items = gplus.activities().search(query=SEARCHSTRING).execute().get('items',[])

for data in items:
	post = ' '.join(data['title'].strip().split())
	if post: 
		try:
			print('Author: ', data['actor']['displayName'])
			print('   Title: ',data['title'].encode("utf-8"))
			print ('SUMMARY: ',(data['actor']['displayName'], data['published'], post))
			print(' ')
		except:
			print('Something went wrong ', sys.exc_info()[0])

print("*** In conclusion, this is is how to use Google API to Plus. I have no idea what the search looks for")