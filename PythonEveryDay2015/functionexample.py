# Example of how functions work   
# From http://www.stavros.io/tutorials/python/
# Typer: Ginny C Ghezzo 
# What I learned:   

def passing_example(a_list, an_int=2, a_string="default"):
	a_list.append("New item") 
	print("This is the value of an_int default %s " %an_int)
	an_int = 4 
	return a_list, an_int, a_string

print("Start")
print(passing_example([1,2,3]))
print("end")