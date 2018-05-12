# Program the Einstein Riddle 
# Note: This program does not work, but it was fun trying 
# Who has the fish?
''' Rules 
1. The British man lives in the red house. 
2. The Swedish man has a dog for a pet. 
3. The Danish man drinks tea. 
4. The green house is to the left of the white house. 
5. The owner of the green house drinks coffee. 
6. The person that smokes Pall Mall has a bird. 
7. The owner of the yellow house smokes Dunhill. 
8. The person that lives in the middle house drinks milk. 
9. The Norwegian lives in the first house. 
10. The person that smokes Blend, lives next to the one that has a cat. 
11. The person that has a horse lives next to the one that smokes Dunhill. 
12. The one that smokes Bluemaster drinks beer. 
13. The German smokes Prince. 
14. The Norwegian lives next to a blue house. 
15. The person that smokes Blend, has a neighbour that drinks water.
'''

row = 30
column = 30						# no idea why I need this 
color = 0
nationality = 5
animal = 10
drink = 15
smoke = 20 
house = 25
blue, green, red,white, yellow = 0, 1, 2, 3, 4 
brit, dan, ger, nor, swe = 5,6,7,8,9
cat,dog,bird,fish,horse = 10,11,12,13,14
tea,coffee,milk,water, beer = 15,16,17,18,19
blend,dunhill,master,pall,prince  = 20,21,22,23,24
one,two,three,four,five = 25,26,27,28,29
name = ['blue', 'green', 'red','white', 'yellow', 'brit', 'dan', 'ger', 'nor', 'swe', 'cat','dog','bird','fish','horse', 'tea','coffee','milk','water', 'beer','blend','dunhill','master','pall','prince', 'one','two','three','four','five' ]

myarray = [ (['NA'] * column) for row in range(row) ]
# Set the self to True (red is red, etc)
start = 0
end = 30
while start < end:
	for x in range(start,start+5):
		for y in range(start,start+5):
			myarray[x][y] = False 
			myarray[y][x] = False 
	start += 5

for x in range(row):
	myarray[x][x] = True
print("This should be true: ", myarray[red][red])
print("This should be false: ", myarray[red][blue])

def summary(this):
	has, hasnot, unknown = [], [], []

	for x in range(30):
		if myarray[this][x] == True:
			has.append(name[x])
		elif myarray[this][x] == False: 
			hasnot.append(name[x])
		else: 
			unknown.append(name[x])
	print(name[this], " has ", has)
	print(name[this], " does not have ", hasnot)
	print(name[this], " does not know ", unknown)

def grid():
	line = ''
	for x in range(30):
		for y in range(30):
			if myarray[x][y] == True:
				line = ''.join([line,'O'])
			elif myarray[x][y] == False:
				line = ''.join([line,'X'])
			else: 
				line = ''.join([line,' '])
		print(str(line))
		print(" ")

def blank(this,start):
	end = start + 5 
	print("This and start and end ", this, start, end)
	try:
		for x in range(start,end):
			if myarray[x][this] == 'NA':
				myarray[x][this] = False
			if myarray[this][x] == 'NA':
				myarray[this][x] = False	
	except: 
		print('What happened? ', x, this)

# 1. The British man lives in the red house. 
blank(red,nationality)
blank(brit,color)
myarray[brit][red] = True
myarray[red][brit] = True
# 2. The Swedish man has a dog for a pet. 
blank(dog,nationality)
blank(swe,animal)
myarray[swe][dog] = True
myarray[dog][swe] = True
# 3. The Danish man drinks tea. 
blank(dan,drink)
blank(tea,nationality)
myarray[dan][tea] = True
myarray[tea][dan] = True
# 4. The green house is to the left of the white house. 
myarray[green][five] = False
myarray[five][green] = False
myarray[coffee][five] = False
myarray[five][coffee] = False
myarray[white][one] = False
myarray[one][white] = False
# 5. The owner of the green house drinks coffee. 
blank(green,drink)
blank(coffee,color)
myarray[green][coffee] = True
myarray[coffee][green] = True
# 6. The person that smokes Pall Mall has a bird. 
blank(bird,smoke)
blank(pall,animal)
myarray[pall][bird] = True
myarray[bird][pall] = True
# 7. The owner of the yellow house smokes Dunhill. 
blank(yellow,smoke)
blank(dunhill,color)
myarray[yellow][dunhill] = True
myarray[dunhill][green] = True
# 8. The person that lives in the middle house drinks milk. 
blank(three,drink)
blank(milk,house)
myarray[three][milk] = True
myarray[milk][three] = True
myarray[green][three] = False
myarray[three][green] = False
myarray[white][four] = False
myarray[four][white] = False
# 9. The Norwegian lives in the first house. 
blank(one,nationality)
blank(nor,house)
myarray[one][nor] = True
myarray[nor][one] = True
myarray[white][nor] = False
myarray[nor][white] = False
# 10. The person that smokes Blend, lives next to the one that has a cat. 
myarray[cat][blend] = False
myarray[blend][cat] = False
# 11. The person that has a horse lives next to the one that smokes Dunhill. 
myarray[horse][dunhill] = False
myarray[dunhill][horse] = False
# 12. The one that smokes Bluemaster drinks beer. 
blank(beer,smoke)
blank(master,drink)
myarray[master][beer] = True
myarray[beer][master] = True
# 13. The German smokes Prince. 
blank(ger,smoke)
blank(prince,nationality)
myarray[ger][prince] = True
myarray[prince][ger] = True
# 14. The Norwegian lives next to a blue house. 
myarray[nor][blue] = False
myarray[blue][nor] = False
# 15. The person that smokes Blend, has a neighbour that drinks water.
myarray[water][blend] = False
myarray[blend][water] = False

print("This could be brit row ", myarray[brit])

for x in range(30):	
	for y in range(30):
		if myarray[x][y] == True:
			if (x == y) == False:
				print("The  ", name[x], " has a ", name[y])
for x in range(30):
	print('***** ', name[x], '******')
	summary(x)

grid()