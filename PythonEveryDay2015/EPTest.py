# Figure out how to contact the EventBrite recruiter 
# http://www.pydanny.com/want-to-work-for-eventbrite.html
# Dev: Ginny C Ghezzo 
# What I learned: Someone is clever! 

# Input the number, turn into char, launch the webpage, find new puzzle  
import webbrowser
import requests 						# Better HTTP then urllib2 
import sys 
from cryptography.fernet import Fernet		# encryption with key 

encrypted_string = 'wEFOJQ340R1JUPEFJEWICOK=oijqwpef39jfwfjwefp99'

if len(sys.argv) > 1:
	user = sys.argv[1]
	pw = sys.argv[2]
# Todo add error checking 

# Why yes, I would love a massage! Thank you!! 
def get_message():
	r = requests.get('https://gist.githubusercontent.com/pydanny/49ef4971f1292c8eadae/raw/48cca5b2855535eb5d822c96da5c34ee77177256/gistfile1.txt') 
	return r.content  # R 
# This is a better version of findClue1 :) 
def get_url(numbers):
	return ''.join([chr(x) for x in numbers]) 

def main():
	keyNum = [104, 116, 116, 112, 115, 58, 47, 47, 103, 105, 115, 116, 46, 103, 105, 116, 104, 117, 98, 117, 115, 101, 114, 99, 111, 110, 116, 101, 110, 116, 46, 99, 111, 109, 47, 112, 121, 100, 97, 110, 110, 121, 47, 102, 100, 101, 54, 98, 48, 101, 49, 97, 54, 51, 99, 49, 56, 101, 51, 52, 51, 101, 51, 47, 114, 97, 119, 47, 57, 56, 97, 54, 55, 99, 57, 55, 52, 54, 101, 52, 57, 54, 48, 49, 102, 50, 54, 53, 49, 56, 101, 54, 98, 101, 100, 51, 101, 53, 48, 52, 56, 48, 56, 50, 54, 99, 98, 56, 47, 103, 105, 115, 116, 102, 105, 108, 101, 49, 46, 116, 120, 116] 
	url = get_url(keyNum)
	r = requests.get(url)			# 
	key = r.content					# what is at that page 
	f = Fernet(key) 
	message = get_message()
	print(f.decrypt(message))

def findClue1():
	code = [104, 116, 116, 112, 115, 58, 47, 47, 103, 105, 115, 116, 46, 103, 105, 116, 104, 117, 98, 46, 99, 111, 109, 47, 112, 121, 100, 97, 110, 110, 121, 47, 97, 56, 55, 100, 57, 54, 49, 54, 102, 49, 50, 55, 52, 48, 48, 97, 57, 55, 97, 52]
	blank =''		# Note, this is NOT NEEDED , just use ''.join ... 
	codeC = []
	for i in code: 
		codeC.append(chr(i))

	url = blank.join(codeC)
	print(url)
	webbrowser.open(url, 1)

findClue1()	
if __name__ == "__main__":
	main()