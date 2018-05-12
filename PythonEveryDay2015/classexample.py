# Example of how class and enheritance work   
# From http://www.stavros.io/tutorials/python/
# Typer: Ginny C Ghezzo 
# What I learned:   

class MyClass(object): 
	common = 10 
	def __init__(self): 
		self.myvariable = 3
	def myfunction(self, arg1, arg2):
		return self.myvariable

class OtherClass(MyClass):
	def __init__(self, arg1):
		self.myvariable = 3
		print arg1


ci = MyClass()
ci2 = MyClass()
print("Myfunction: %s" %ci.myfunction(1,5))
print("common ci: %s" %ci.common)
print("common ci2: %s" %ci2.common)
MyClass.common = 30 
print("new common ci: %s" %ci.common)
print("new common ci2: %s" %ci2.common)
ci.common = 10 
print("class name change common ci: %s" %ci.common)
print("class name change common ci2: %s" %ci2.common)
MyClass.common = 50 
print("class name change common ci: %s" %ci.common)
print("class name change common ci2: %s" %ci2.common)

ci = OtherClass("hello")
print (ci.myfunction(1,2))
ci.test = 10 
print(ci.test)


print("The end")