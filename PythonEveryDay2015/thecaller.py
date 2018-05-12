# The caller 
# I don't really understand this well. 
from LearnDecorators import my_decorator 

@my_decorator 
def just_some_function():
	print("Whee .. from the caller")
just_some_function()