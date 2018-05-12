# Learning Python the hard way - http://learnpythonthehardway.org/book/ex10.html
# Exercise 10 -  What was that? 
# \\ backslash 
# \' single quote
# \" double quote 
# \a ASCII Bell 
# \b backspace 
# \f formfeed 
# \n linefeed
# \N(name) Character named name in the unicode database 
# \r ASCII carriage REturn 
# \r Tab 
# \v vertical tab 

tabby_cat = "\tI'm tabbed in." 
persion_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat Food 
\t* Fishies 
\t* Catnip\n\t* Grass
""" 

mad_cat = '''
This is a test 
of the triple single quote 
'''

print tabby_cat 
print persion_cat
print backslash_cat
print fat_cat 
print mad_cat
print "\a" 

#while True: 
#   for i in ["/", "-", "|", "\\", "|"]:
#      print "%s\r" % i,


