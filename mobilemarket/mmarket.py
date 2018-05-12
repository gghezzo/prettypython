# name: MMarket.py 
# description: Read address off pictures (OCR) and map out the route
# 

from PIL import Image 
import pytesseract 
import googlemaps
import sys 
from datetime import datetime
from os import listdir 

try:
	f = open('mykey.txt')
	mykey = f.readline().strip()	
except (IOError, ValueError): 
	print("An I/O Error or Value occurred.force the key ")
	mykey = input("Please enter your google maps key ")
print('Key = ' + mykey)

# This is done because of a windows issue. Not needed on Linux 
pytesseract.pytesseract.tesseract_cmd = 'c:/Tesseract-OCR/tesseract'

# Get the pictures 
pics = []
for f in (listdir(path='.')):
	if '.jpg' in f: 
		pics.append(f)
print("This is the potential clients", pics)

# Make a list of addresses 
clientList = []
for f in pics: 
	img = Image.open(f)
	label = pytesseract.image_to_string(img)
	address = label.splitlines()[2] + ', ' + label.splitlines()[3]
	clientList.append(address)
print(clientList)

# Do I need to make these into lat\lngs? 

# Create a map of them 
home = "2403 Englewood Ave, Durham, NC 27705"
now = datetime.now()
wp=[]
try: 
	gmapsC = googlemaps.Client(key=mykey)
	directions = gmapsC.directions("Duke Memorial", home, mode="driving", waypoints=wp, optimize_waypoints=True, departure_time=now)
except:
	e = sys.exc_info()[0]
	print('There was a problem with googlemaps',e)

print(directions[0]['summary'])