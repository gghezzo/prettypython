# Check your IP address  
# From http://www.pythonforbeginners.com/code-snippets-source-code/check-your-external-ip-address
# Typer: Ginny C Ghezzo 
# What I learned:  Python 2 vs 3 sucks! Have to be particular about string vs binary. 
# TODO: Why did I have to import urllib.request instead of just urllib? 
# TODO: Add this to the time window 
# TODO: add a location look up based on address 


import urllib
import urllib.request
import re 
print ("Try to open this URL to get the IP Address")
url= "http://checkip.dyndns.org"
print(url)
# request = urllib.urlopen(url).read()
f = urllib.request.urlopen(url).read()
print(f)
theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", str(f))
print("Your IP Address is: ", theIP)