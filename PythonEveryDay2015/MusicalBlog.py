# Make a list of all the songs I have used on my blog  http://gghezzo.blogspot.com/ 
#	get access to my google blog 
#	for every post, find the reference to the youtube video 
#	Save this list to a file [Bonus: Make a Youtube ]
# Developer: Ginny C Ghezzo 
# References:  
#	BAD? Blogger API Client Library for Python : https://developers.google.com/blogger/docs/3.0/api-lib/python?hl=en
#Comments: The API description made me fall in love, even more with Google. 
#Comment: Oops I did a 'pip install -t lib gcloud' and got a error 1 . Same issues as my pandas MS Visual C++ unable to find vcvarsall.bat

import apiclient.discovery		# No idea : http://wescpy.blogspot.com/2014/09/simple-google-api-access-from-python.html
from apiclient.discovery import build 

SERVERKEY = input("Shhh What is your API Blogger Server Key (hint AIz) : ")
print(SERVERKEY)
Service = build('blogger', 'v3', developerKey=SERVERKEY)	#API=plus and VERSION=v1
print(Service)