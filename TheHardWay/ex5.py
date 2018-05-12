# http://learnpythonthehardway.org/book/ex5.html
# Conversion Type Integers (d, i), Repr (r), string (s), float (e, E, f, F, g, G), char (c) 
# octal (o) decimal (u) 
# http://docs.python.org/release/2.4.4/lib/typesseq-strings.html

name = "Ginny Ghezzo" 
age = 43
height = 66 #inches 
weight = 160 # lbs
eyes = 'Blue' 
teeth = "White" 
hair = "Red" 
  
print "Let's talk about %r." %  name
print "She is %r inches tall." %  height
print "She is %d pounds" %  weight
print "Actually that is not too heavy." 
print "She has %s color eyes and %s  hair" % ( eyes,  hair) 
print "Her teeth are usually %s depending on the coffee." %  teeth 

# this line is tricky, try to get it exactly right 
print "If I add %d, %d, and %d I get %d." % ( age,  weight,  height,  age +  height +  weight)

# convert inches to centimeters  1 inch = 2.54 cm
i = 5 #inches
print "( %d inches as centimeters = %f)" % (i, i * 2.54) 

# convert pounds to kilo 
p = 160 # pounds 
print " %d pounds as kilos is %f " % (p, p / 2.2046)

