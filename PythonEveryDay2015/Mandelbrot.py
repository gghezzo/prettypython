# More tkinter  - https://www.youtube.com/watch?v=ES-yKOYaXq0
# From http://code.activestate.com/recipes/579048-python-mandelbrot-fractal-with-tkinter/
# Typer: Ginny C Ghezzo 
# What I learned: Antoni Gual via writes tight code! 
# 		.join will take a sequence and return a string, seperator.join(sequence)
#		using clock to keep elapsed time (print(clock()-t1, ' seconds'))
# todo: think about changing the return to be more readable, 


from tkinter import Tk, Canvas, PhotoImage, NW, mainloop

from time import clock 

def mandel_pixel(c):
	# calculate the color index of the mandelbrot plane point
	maxIt = 256
	z = c 			#huh
	for i in range(maxIt):
		a = z*z
		z=a+c
		if a.real >= 4.:
			return i 
	return 256

def mandelbrot(xa,xb,ya,yb,x,y):
	# returns a mandelbrot in a strong for TK PhotoImage
	# color string table in Photoimage format #RRGGBB. shades of red based on the loop 
	# examples #ff0000 or #de0000 
	clr=[ ' #%02x%02x%02x' % (int(255*((i/255)**.25)),0,0) for i in range(256)]
	clr.append(' #000000')					#append the color of the centre as index 256 (black)
	# calculate mandelbrot x,y coordinates for each screen pixel 
	xm=[xa + (xb - xa) * kx /x for kx in range(x)]
	ym=[ya + (yb - ya) * ky /y for ky in range(y)]
	# build the PhotoImage string by calling mandel_pixel to index in the color table 
	return " ".join((("{"+" ".join(clr[mandel_pixel(complex(i,j))] for i in xm))+"}" for j in ym ))

#window size 
x = 640
y=480
# corners of the mandelbrot plan to display 
xa = -2.0; xb = 1.0 
ya = -1.27; yb = 1.27 

#Tkinter window 
window = Tk()
canvas = Canvas(window, width = x, height = y, bg= "#000000"); canvas.pack()		#black
img = PhotoImage(width=x, height=y)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

#do the mandelbrot!! 
t1=clock()
img.put(mandelbrot(xa,xb,ya,yb,x,y))
print(clock()-t1, ' seconds')

mainloop()



