# Various little programs to try 
# From https://wiki.python.org/moin/SimplePrograms
# Typer: Ginny C Ghezzo 
# What I learned: Had to close after the write, had to open string not binary, 

import csv 
# write stock data as comma-seperated values 
f = open('stocks.csv', 'w', newline='')
writer = csv.writer(f, delimiter=",")
writer.writerows([
	('ticker', 'name', 'price', 'change', 'pct'),
	('GOOG', 'Google, Inc.', 505.24, 0.47, 0.09), 
	('IBM', 'IBM, Corp.', 167.55, 0.33, 1.22), 
	('CNET', 'CNET Netwroks, Inc.', 8.24, -0.13, -1.49) 
])
f.close()

# read stocks data, print status message ticker, name, price, change, pct
# ticker, name, price, change, pct
f = open('stocks.csv', 'rt')
stocks = csv.DictReader(f, delimiter=',')
print(stocks.fieldnames)

print("Loop through the stocks %s", str(stocks)) 
try:
	for ticker, name, price, change, pct in stocks: 
		print( 'This is important %s is %s ' % (name, price))
		break
finally:
	print("finally!!")
f.close()


with open('stocks.csv') as csvfile:
	stocks = csv.reader(csvfile)
	for row in stocks:
		print(row)




