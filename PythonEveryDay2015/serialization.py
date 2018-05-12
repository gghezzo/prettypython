# Example of how here is how serializing with file I/O    
# From http://www.stavros.io/tutorials/python/
# Typer: Ginny C Ghezzo 
# What I learned:  pickling is a common term in python, dumping is creating a pickle in a file! 
# you have to use // not \\ 

import pickle 
import os 
mylist = ["This", "is", 4, 13327]
# open the file c:\binary.dat for writing. The letter r before the 
# filename string is used to prevent backslash escaping. 
myfile = open(r"c:binary.dat", "wb")
print(myfile)
pickle.dump(mylist, myfile )
myfile.close()

myfile = open(r"C:text.txt", "w")
myfile.write("This is a sample string")
myfile.close()

myfile = open(r"C:text.txt")
print(myfile.read())
myfile.close()

# Open the file for reading. 
myfile = open(r"c:binary.dat", "rb")
loadedlist = pickle.load(myfile)
myfile.close()
print(loadedlist)



