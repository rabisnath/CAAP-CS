# Alex Bisnath
# Lab 4
# August 5

# Imports the turtle graphics module
import turtle
import math
import random
from random import randint
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(10)
myPen.color("#000000")
turtle.delay(0)

width, height = turtle.screensize()

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
	myPen.forward(intRadius)
	myPen.pendown()
	n = intRadius #number of sides in our polygon approximation of a circle
	theta = (2 * math.pi) / float(n) #the external angle of the polygon
	distance = math.sqrt( (2*(intRadius**2)) * (1 - math.cos(theta)) ) #side length
	for i in range(int(n)):
		myPen.forward(distance)
		myPen.left(theta * (180 / math.pi))
	myPen.end_fill()
	myPen.penup()

def triangle(intLength): #This can be an equilateral triangle
	myPen.begin_fill()
	myPen.pendown()
	for i in range(3):
		myPen.forward(intLength)
		myPen.left(120)
	myPen.end_fill()
	myPen.penup()

#def save_image(): # saves the screen to an image/vector file



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
			#myPen.right(theta)
			draw_fractal_tree(branching_factor, theta*(0.75), size * shrinking_factor, shrinking_factor)
			myPen.forward(-1 * size)
			#myPen.left(theta)

			myPen.penup()
			
		#myPen.right(theta * ((branching_factor / 2) ))

def indv_dec_to_hex(x):
	numerals = '0123456789ABCDEF'
	sixteens = int(math.floor(x/16))
	ones = x % 16
	a = numerals[sixteens]
	b = numerals[ones]
	return a + b

def full_dec_to_hex(r, g, b):
	R, G, B = indv_dec_to_hex(r), indv_dec_to_hex(g), indv_dec_to_hex(b)
	return "#" + R + G + B

def hex_to_dec(string):
	sub_strs = []
	for i in range(1, len(string), 2):
		sub = ""
		sub += string[i]
		sub += string[i+1]
		sub_strs.append(sub)

	numerals = '0123456789ABCDEF'
	rgb_values = []
	for hexstring in sub_strs:
		rgb_values.append( numerals.find(hexstring[0]) * 16 + numerals.find(hexstring[1]) )

	return rgb_values[0], rgb_values[1], rgb_values[2]

def get_random_hex():
	output = "#"
	for i in range(3):
		output += indv_dec_to_hex(randint(0,255))
	return output


def make_pallet(num, starting_hex, rvel, gvel, bvel): #returns a pallet of colors starting at the starting_hex, incrementing at a speed based on the velocity
	r, g, b = hex_to_dec(starting_hex)
	components = [r, g, b]
	velocities = [rvel, gvel, bvel]

	pallet = []
	while len(pallet) < num:
		for i in range(len(components)):
			after_image = components[i] + velocities[i]
			if  after_image > 255 or after_image < 0:
				velocities[i] = velocities[i] * -1
			after_image = components[i] + velocities[i]
			components[i] = after_image
		#print(components)
		color = full_dec_to_hex(components[0], components[1], components[2])
		pallet.append(color)

	return pallet

def make_diag_grid(size, num_colors):
	grid = []
	icount = 0
	for i in range(size):
		row = []
		jcount = icount % num_colors
		for j in range(size):
			row.append(jcount % num_colors)
			jcount+=1
		grid.append(row)
		icount+=1
	return grid

def draw_rainbow_grid(size, num_colors, varience):
	start = get_random_hex()
	varience = int(varience)
	rv, gv, bv = randint(-1*varience, varience), randint(-1*varience, varience), randint(-1*varience, varience)
	pallet = make_pallet(num_colors, start, rv, gv, bv)
	grid = make_diag_grid(size, num_colors)

	draw(pallet, grid)

def make_empty_grid(order): #a 3x3 grid has order 1, a size 5 grid has order 2, this construction is conveinient as the order is the index of the center row and column
	size = 2*order + 1
	grid = []
	for i in range(size):
		row = []
		for j in range(size):
			row.append(0)
		grid.append(row)
	return grid

def distance_from_center(row, column, grid_order):
	return int(math.fabs(row - grid_order) + math.fabs(column - grid_order))

def make_flower_grid(order, num_colors):
	grid = make_empty_grid(order)
	for rowid in range(2*order + 1):
		for itemid in range(2*order + 1):
			distance = distance_from_center(rowid, itemid, order)
			grid[rowid][itemid] = distance % num_colors
	return grid

def draw_flower_grid(order, num_colors, varience):
	start = get_random_hex()
	varience = int(varience)
	rv, gv, bv = randint(-1*varience, varience), randint(-1*varience, varience), randint(-1*varience, varience)
	pallet = make_pallet(num_colors, start, rv, gv, bv)
	grid = make_flower_grid(order, num_colors)

	draw(pallet, grid)

def tile_canvas(drawfunction, tile_size, num_colors, varience):
	myPen.goto(-1*width, height + 50)
	t_height = math.floor(height / (tile_size*boxSize))
	t_width = math.floor(width / (tile_size*boxSize))
	print(t_width )
	order = tile_size
	for x in range(t_width):
		for y in range(t_height + 1):
			drawfunction(order, num_colors, math.ceil(varience*random.uniform(0,1) + 0.25*varience))
		myPen.goto((-1*width) + (x+1)*order*boxSize*2 + (x+1)*boxSize, height+50+(50 * ((x + 1)% 2)))








			

 
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
	#myPen.goto(0,0)
	#myPen.goto(-1*width, height)
	#draw(pallet_1, pixels_1)
	#draw(pallet_2, pixels_2)
	#draw(pallet_3, pixels_3)
	#draw(pallet_4, pixels_4)
	#draw(pallet_5, pixels_5)
	#draw(pallet_6, pixels_6)

	#myPen.color("#DD00FF")
	#circle(200)
	#triangle(200)

	#draw_fractal_tree(branching_factor, theta, size, shrinking_factor)
	#draw_fractal_tree(2, 30, 150, 0.5)

	#print(hex_to_dec("#FFFFFF"))
	#print(full_dec_to_hex(255,255,255))
	#print(make_pallet(16, "#0000FF", 10, -15, 20))

	#draw_rainbow_grid(24, 6, 50)
	#draw_flower_grid(10, 6, 50)

	#MY TWO DRAWINGS ARE HERE:
	tile_canvas(draw_flower_grid, 5, 6, 50)
	
	#tile_canvas(draw_rainbow_grid, 10, 6, 50)

	# You need this to prevent the window from closing after drawing
	turtle.done()

main()