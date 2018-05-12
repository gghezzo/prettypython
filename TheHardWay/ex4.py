# Learning Python the hard way - http://learnpythonthehardway.org/book/ex4.html
# Exercise 4 - Variables and Names  

# there are 200 cars 
cars = 100
# four people can sit in each car 
space_in_a_car = 4.0 
# there are 30 available drivers 
drivers = 30
# there are 90 passangers. Not sure if that includes drivers
passengers = 90 
# lack of drivers means cars sit
cars_not_driven = cars - drivers
# this is dumb.  Cars don't need to need drivers
cars_driven = drivers 
# another weird equation .  number of car drivers times spaces 
carpool_capacity = cars_driven * space_in_a_car 
# average number of people who have to sit in the car. 
average_passengers_per_car = passengers / cars_driven 

print "There are ", cars, "cars available" 
print "There are only ", drivers, " drivers available" 
print "There will be ", cars_not_driven, " empty cars today." 
print "We can transport ", carpool_capacity, " people today." 
print "We have ", passengers, " to carpool today." 
print "We need to put about ", average_passengers_per_car, " in each car." 


