# Regex class - Trey ? 
# From https://regex.netlify.com/exercises
# Coder : Ginny C Ghezzo 
# What I learned: 

import re 
def has_vowel( word ): 
		if (re.search(r'[aeiou]',word) == None):
			return False
	return True 

print("Dog", has_vowel("Dog"))