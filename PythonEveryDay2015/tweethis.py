# Paly with Twitter  
# https://code.google.com/p/python-twitter/
# Typer: Ginny C Ghezzo 
# What I learned: 
#Keys ? What keys? https://apps.twitter.com/app/8734762/keys (at, ATS, CS, CK) 
from twitter import *  

string = input('Add them now (token, tokenkey, consecret, consecretkey : ')
all_keys = string.split(",")
print('The tokens you gave are: ',all_keys)
t = Twitter(auth=OAuth(all_keys[0],all_keys[1],all_keys[2],all_keys[3])) 
last = t.statuses.home_timeline(count=1)
print('Last tweet: ',last[0]['user']['screen_name'])

me = t.search.tweets(q='GinnyGhezzo')
print('My last tweet: ', str(me['statuses'][0]['text']))
print('My 2nd to last tweet ', me['statuses'][1]['text'])
# t.statuses.update(status='You do not want to do this') 