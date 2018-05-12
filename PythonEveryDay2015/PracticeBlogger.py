# Try to use google api for blogger 
# Developer: Ginny C Ghezzo 
# References:  https://developers.google.com/blogger/docs/3.0/reference/posts/list
# https://console.developers.google.com/apis/credentials?project=testingbloggerapi-1056 


import apiclient.discovery		
from apiclient.discovery import build 
import sys
import pafy
import logging 
import re

SERVERKEY = input("Shhh What is your API Blogger Server Key (hint AIz) : ")
maxRes = input("How many posts ? ")
if maxRes == '': 
	maxRes = '10'
maxRes = int(maxRes)
logging.getLogger().setLevel(logging.ERROR)
gblog = build('blogger', 'v3', developerKey=SERVERKEY)	# produces a discover.Resouce.object
# search(), which lets you query public activities
# My blog : gghezzo@us.ibm.com

items = gblog.posts().list(blogId='2040322735491116476').execute().get('items',[])

for data in items:
	post = ' '.join(data['title'].strip().split())
	if post: 
		try:
			print('Author: ', data['author']['displayName'])
			print(data.keys())
			print(' ')
		except:
			print('Something went wrong ', sys.exc_info()[0])

print('*** Now trying it for gghezz0 ***')
ppitems = gblog.posts().list(blogId='17274848',maxResults=maxRes).execute().get('items',[])

count = 0 
list = []
#Need a better parse maybe embed vs watch 
for data in ppitems:
	if data['content'].find("www.youtube.com") > 0 and data['content'].find("?feature") >0: 
		count += 1
		try:
			print(str(count),'Published: ', data['published'])
			print('   Blog Title: ', data['title'])
			content = data['content']
			url = "https://" + (content[content.find("www.youtube.com/embed"):content.find("?feature")])
			video = pafy.new(url)
			print('   Video Name: ',video.title)
			print('   Video URL: ',url)
			list.append(video.title)
			print(' ')
		except:
			print('Something went wrong ', sys.exc_info()[0])
print(list)

hits = []
chkStr = input('What to check for a song? (q)? ')
while chkStr != 'q':
	for boo in list:
		if re.search(chkStr, boo, re.IGNORECASE):
			hits.append(boo)
	print(hits)
	hits.clear()
	chkStr = input('What to check for a song? (q)? ')
