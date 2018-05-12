# Text me when I need to bring in the plants 
# From my brain
# Typer: Ginny C Ghezzo 
# What I learned: OpenWeatherMap, SMS, 

from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import pyowm 
from datetime import datetime 
from dateutil.tz import tz, tzlocal
import sys

DURM = 4464368 
cred = {}	## probably should not be global 

# Get the authentication and variables 
# TODO: Don't use globals ... fix this 
# Thank you Lauritz V. Thaulow - http://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file 
def get_credentials(): 
	with open("cred.txt") as myfile:
		for line in myfile:
			name, var = line.partition("=")[::2]
			cred[name.strip()] = var.strip()
	return()

# Note: The message has satus including when 
def textMe(msg): 
	try: 
		twilioCli = TwilioRestClient(cred["twilio_accountSID"], cred["twilio_authToken"])
		message = twilioCli.messages.create(to=cred["my_phone"], from_=cred["twilio_phone"], body=msg)
	except TwilioRestException as e: 
		print('Boo', e)
	return()

def isItFreezing (): 
	owm = pyowm.OWM(cred["owm_key"])
	msg = 'Let me check'
	isCold = False
	current_weather = owm.weather_at_id(DURM).get_weather().get_temperature('fahrenheit')['temp']
	today_forecast = owm.daily_forecast('Durham, us', limit=1).get_forecast().get_weathers()[0].get_temperature('fahrenheit')['min']
	if (current_weather < 40): 
		msg = 'Damn Girl! Bring in the poor plants. It is now ' +  str(current_weather) 
		isCold = True
	elif ( today_forecast < 40):
		msg = 'Not Cold now (' + str(current_weather) + ') , but the forecast predicts a low of ' + str(today_forecast)
		isCold = True
	else:
		msg = 'Keep the Plants Outside and enjoy the night. It will only get down to ' + str(today_forecast)
		isCold = False 

	textMe(msg)
	return(isCold)



# ?poll? the OpenWeatherMap once a day: at a time? 
# At 3pm check the current temp and the projected low 
# If it is less then 35F? text me (or )
get_credentials()
print('accountSID', cred["twilio_accountSID"], 'authtoke- ', cred["twilio_authToken"])
print('to=',cred["my_phone"], 'from_=',cred["twilio_phone"])
if (isItFreezing()):
	print('Yes it is Freezing ')
else:
	print('Nope it is not Freezing')
