# Playing around with CSV files 
# From my brain 
# Typer: Ginny C Ghezzo 
# What I learned: join seperator.join(sequence) (exm ', '.join(['a', 'b'])), Use DictReader instead of reader
# DictWriter = "Create an object which operates like a regular writer but maps dictionaries onto output rows" 
# I am surprised I did not have to import sys 
# TODO: Pass in the file name, 
# TODO: Confirm that if I am using a DictReader then I have to use header strings instead of offsets 
# TODO: #Do I need to close the write file? 

import csv
f = open(r'C:\learnPython\TechGirlzAttendance\report-linux.csv')
csv_f = csv.reader(f)
csvdict_f = csv.DictReader(f)

#
# Basic Read 
#for row in csv_f:
#	print(row[6] + ' ' + row[7] + ' ' + row[3] + ' '+ row[4] )

print("Why is this not working")
f.seek(0)

attendee_idset = []
for row in csv_f:
	if row[7] == 'Attending':
		print(row[6] + ' ' + row[3] + ' '+ row[4] )
		attendee_idset.append(row[6])

print("This is the list of No shows")
print(attendee_idset)

f.seek(0)
mydict = dict((rows[6],(rows[3]+ ' ' + row[4])) for rows in csv_f)
print("This is a dictionary of all the items ")
print(mydict)

f.seek(0)
anotherdict = {}
for row in csv_f:
	if row[7] == 'Attending':
		key = row[6]
		anotherdict[key] = (row[3]+ ' ' + row[4])
print("This is a dictionary of those who missed")
print(anotherdict)
for x in anotherdict: 
	print(anotherdict[x])
print('The total number of No Shows ', len(anotherdict))

# Try it with the DictReader 
f.seek(0)
print('\n\nOne more time with DictReader ')
event = None
for row in csvdict_f:
	if event is None: event = row['Event Name']
	if row['Attendee Status'] == 'Attending':
		key = row['Attendee #']
		anotherdict[key] = (row['First Name']+ ' ' + row['Last Name'])

for x in anotherdict: 
	print(anotherdict[x])
print('The total number of No Shows ', len(anotherdict))
f.close()

#Now time to try some Writing 
with open('temp.csv', 'w') as csvfile:
	fieldnames = ['Attendee #', 'Last Name', 'First Name', 'Missed Events', 'Total']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for x in anotherdict:
		writer.writerow({'Attendee #': x, 'Last Name': anotherdict[x], 'First Name': '123', 'Missed Events':event, 'Total': 1})

#Do I need to close the write file? 




