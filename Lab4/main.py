# YOUR NAME
# Assignemnt X
# Date Due

# Imports the turtle graphics module
import turtle
import math
from random import randint
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(10)
myPen.color("#000000")
turtle.delay(20)

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0) 

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)       

# Here is an example of how to draw a box using the box function      
# Comment this out when you draw your own images
#box(boxSize)
 

# Challenge functions (2 bonus pts each) 
# You need to make shapes with each
def circle(intRadius):
	myPen.begin_fill()
	myPen.penup()
	myPen.setheading(0)
	myPen.forward(intRadius)
	myPen.setheading(90)
	myPen.pendown()
	n = intRadius #number of sides in our polygon approximation of a circle
	theta = (2 * math.pi) / float(n) #the external angle of the polygon
	distance = math.sqrt( (2*(intRadius**2)) * (1 - math.cos(theta)) ) #side length
	for i in range(int(n)):
		myPen.forward(distance)
		myPen.left(theta * (180 / math.pi))
	myPen.end_fill()
	myPen.penup()
	myPen.setheading(0)

#def triangle(intLength): #This can be an equilateral triangle

#def save_image(): # saves the screen to an image/vector file

def dec_to_hex(x):
	numerals = '0123456789ABCDEF'
	sixteens = int(math.floor(x/16))
	ones = x % 16
	a = numerals[sixteens]
	b = numerals[ones]
	return a + b

#def draw_fractal_tree(branching_factor, shrinking_factor, theta, scale, levels):
#	r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
#	r, g, b = dec_to_hex(r), dec_to_hex(g), dec_to_hex(b)
#	myPen.color("#" + r + g + b)
#	myPen.pendown()
#	myPen.forward(scale)

#	draw_branch(branching_factor, shrinking_factor, theta, scale, levels - 1, r, g, b)


#def draw_branch(branching_factor, shrinking_factor, theta, scale, levels, r, g, b):

#	for i in range(levels):
		
#		myPen.left(theta * math.floor(branching_factor / 2))

#		for j in range(branching_factor):
			#change color here maybe
#			myPen.forward(scale)
#			draw_branch(branching_factor, shrinking_factor, theta, scale, levels - 1, r, g, b)
#			myPen.penup()
#			myPen.forward(-1*scale)
#			myPen.right(theta)
#			myPen.pendown()

#		myPen.left(theta * branching_factor / 2)
		#myPen.forward(-1*scale)
#		scale *= shrinking_factor
#		theta *= 1 + (1 / levels)

# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the oen down and it draws as it moves
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()

def draw_fractal_tree(branching_factor, theta, size, shrinking_factor):
	if size > 10:
		myPen.left(theta * ((branching_factor / 2) ))
		for i in range(branching_factor):
			myPen.pendown()
			myPen.forward(size)
			draw_fractal_tree(branching_factor, theta*(0.75), size * shrinking_factor, shrinking_factor)
			myPen.forward(-1 * size)
			myPen.right(theta)

			myPen.penup()
			
		#myPen.right(theta * ((branching_factor / 2) ))


			

 
# You will save your drawings as lists.
# This first list stores the color values
pallet_1 = ["#FFFFFF" , "#FFFF00" , "#000000" , "#61380B" , "#F4FA58"]
# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list
# Banana
pixels_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,2,2,3,3,2,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,4,1,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,4,1,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,1,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,1,1,2,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,1,3,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Mario
pallet_2 = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]
pixels_2 = [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1]]
pixels_2.append([1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_2.append([1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1])
pixels_2.append([1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1])
pixels_2.append([1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3])
pixels_2.append([1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1])
pixels_2.append([1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1])
pixels_2.append([1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1])
pixels_2.append([1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1])
pixels_2.append([0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0])
pixels_2.append([3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3])
pixels_2.append([3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3])
pixels_2.append([3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3])
pixels_2.append([1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1])
pixels_2.append([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1])
pixels_2.append([0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0])

# Add your own drawings here

# Blinky
pallet_3 = ["#FFFFFF", "#FF0000", "#0000FF"]
pixels_3 = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0]]
pixels_3.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0])
pixels_3.append([0,0,1,1,0,0,1,1,1,1,0,0,1,0])
pixels_3.append([0,1,1,0,0,0,0,1,1,0,0,0,0,0])
pixels_3.append([0,1,1,0,0,2,2,1,1,0,0,2,2,0])
pixels_3.append([1,1,1,0,0,2,2,1,1,0,0,2,2,1])
pixels_3.append([1,1,1,1,0,0,1,1,1,1,0,0,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
pixels_3.append([1,1,0,1,1,1,0,0,1,1,1,0,1,1])
pixels_3.append([1,0,0,0,1,1,0,0,1,1,0,0,0,1])

# Space invader
pallet_4 = ["#FFFFFF", "#FF00FF"]
pixels_4 = [[0,0,1,0,0,0,0,0,0,1,0,0]]
pixels_4.append([0,0,0,1,0,0,0,0,1,0,0,0])
pixels_4.append([0,0,1,1,1,1,1,1,1,1,0,0])
pixels_4.append([0,1,1,0,1,1,1,1,0,1,1,0])
pixels_4.append([1,1,1,1,1,1,1,1,1,1,1,1])
pixels_4.append([1,0,1,1,1,1,1,1,1,1,0,1])
pixels_4.append([1,0,1,0,0,0,0,0,0,1,0,1])
pixels_4.append([0,0,0,1,1,0,0,1,1,0,0,0])

# Mushroom
pallet_5 = ["#FFFFFF", "#000000", "#FF0000"]
pixels_5 = [[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0]]
pixels_5.append([0,0,0,1,1,2,2,2,2,2,0,0,1,1,0,0,0])
pixels_5.append([0,0,1,0,0,2,2,2,2,2,0,0,0,0,1,0,0])
pixels_5.append([0,1,0,0,2,2,2,2,2,2,2,0,0,0,0,1,0])
pixels_5.append([0,1,0,2,2,0,0,0,0,0,2,2,0,0,0,1,0])
pixels_5.append([1,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,1])
pixels_5.append([1,2,2,2,0,0,0,0,0,0,0,2,2,0,0,2,1])
pixels_5.append([1,0,2,2,0,0,0,0,0,0,0,2,0,0,0,0,1])
pixels_5.append([1,0,0,2,2,0,0,0,0,0,2,2,0,0,0,0,1])
pixels_5.append([1,0,0,2,2,2,2,2,2,2,2,2,2,0,0,2,1])
pixels_5.append([1,0,2,2,1,1,1,1,1,1,1,1,1,2,2,2,1])
pixels_5.append([0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0])
pixels_5.append([0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0])
pixels_5.append([0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0])
pixels_5.append([0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0])
pixels_5.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0])

# Happy Face
pallet_6 = ["#FFFFFF", "#000000", "#DDFF00", "#8C6400", "#FF6DE9"]
pixels_6 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_6.append([0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0])
pixels_6.append([0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0])
pixels_6.append([0,0,0,1,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,1,0,0,0])
pixels_6.append([0,0,0,1,2,2,1,1,1,1,0,1,2,2,2,2,2,2,1,1,1,1,0,0,1,2,2,1,0,0,0])
pixels_6.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_6.append([0,0,1,2,2,1,1,1,1,1,0,0,1,2,2,2,2,1,1,1,1,1,0,0,0,1,2,2,1,0,0])
pixels_6.append([0,1,2,2,2,1,1,1,1,0,0,0,1,2,2,2,2,1,1,1,1,0,0,0,0,1,2,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,1,0])
pixels_6.append([1,2,2,2,1,0,0,0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0,0,0,1,2,2,2,1])
pixels_6.append([1,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_6.append([0,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_6.append([0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0])
pixels_6.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,1,0,0])
pixels_6.append([0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,1,2,2,1,0,0])
pixels_6.append([0,0,0,1,2,2,1,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,3,3,1,2,2,1,0,0,0])
pixels_6.append([0,0,0,1,2,2,2,1,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,1,2,2,2,1,0,0,0])
pixels_6.append([0,0,0,0,1,2,2,2,1,1,3,3,3,3,4,4,4,4,4,4,1,1,1,2,2,2,1,0,0,0,0])
pixels_6.append([0,0,0,0,0,1,1,2,2,2,1,1,1,3,4,4,4,4,1,1,1,2,2,2,1,1,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,1,1,2,2,2,2,1,1,1,1,1,2,2,2,2,1,1,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0])
pixels_6.append([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0])


# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
	myPen.setheading(0)
	for row in pixels: #iterating through the rows in the drawing
		for color in row: #iterating over each pixel in a row
			myPen.color(pallet[color]) #setting the color and drawing the pixel
			box(boxSize)
			myPen.forward(boxSize)
		myPen.penup() #moving to draw the next row
		myPen.forward(-1 * len(pixels[0]) * boxSize)
		myPen.setheading(270)
		myPen.forward(boxSize)
		myPen.setheading(0)


# Should give the user a list of the possible drawing pieces you have and ask which one to draw
def main():
	#draw(pallet_1, pixels_1)
	#draw(pallet_2, pixels_2)
	#draw(pallet_3, pixels_3)
	#draw(pallet_4, pixels_4)
	#draw(pallet_5, pixels_5)
	#draw(pallet_6, pixels_6)
	#myPen.color("#DD00FF")
	#circle(400)
	#draw_fractal_tree(branching_factor, shrinking_factor, theta, scale, levels)
	#draw_fractal_tree(3, 0.5, 15, 150, 3)
	#draw_fractal_tree(branching_factor, theta, size, shrinking_factor)
	draw_fractal_tree(2, 30, 150, 0.5)
	# You need this to prevent the window from closing after drawing
	turtle.done()

main()