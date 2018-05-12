# Playing around with Videos
# From my brain 
# Typer: Ginny C Ghezzo 
# What I learned: 

import webbrowser 

url = input("What would you like to open? ")
print("The URL = ", url)
if url == '':
	url = "videoplay.html" 
print(url)
webbrowser.open(url, 1)					# 2 means open in tab 