# How much pocket change do you have 
# From https://www.maketecheasier.com/a-basic-introduction-to-python-3/ by Josh Price
# Typer: Ginny C Ghezzo 
# What I learned: So little :( 
	
total = input("Enter cash amount in dollar: $")
# Get amount in pennies 
pennies = float(total) * 100 
# Change purse (a dictionary of coins)
change = { "quarters" : 0, 	"dimes" : 0, "nickels" : 0, "pennies" : 0}

while pennies > 0: 
	if pennies >= 25:
		change["quarters"] += 1
		pennies -= 25
		continue
	elif pennies >= 10:
		change["dimes"] += 1
		pennies -= 10 
		continue
	elif pennies >= 5:
		change["nickels"] += 1
		pennies -= 5 
		continue 
	else: 
		change["pennies"] = int(pennies)
		pennies = 0 
#print results
print("Q:",change["quarters"])
print("D:",change["dimes"])
print("N:",change["nickels"])
print("P:",change["pennies"])

score = input("Enter score: ")
score = int(score)
if score >= 90:
	grade = 'A' 
elif score >= 80:
	grade = 'B' 
elif score >= 70:
	grade = 'C'
elif score >= 60:
	grade = 'D'
else: 
	grade = 'Fail'
print ("\n\nGrade is: "+ grade)

