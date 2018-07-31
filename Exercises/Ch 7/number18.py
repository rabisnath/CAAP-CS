#this script finds the roots of a quadratic function
import math

def get_roots():
	coefs = input("Enter values for a b and c separated by commas\n")
	#try:
	a, b, c = coefs.split(",")
	a, b, c = int(a), int(b), int(c)

	discrim = b**2 - 4*a*c
	if discrim < 0:
		print("This equation has no real roots")
	elif discrim == 0:
		root = -1 * (b/2*a)
		print("This equation has one real root at " + str(root))
	else:
		root1, root2 = (-1*b + math.sqrt(discrim)) / 2*a, (-1*b - math.sqrt(discrim)) / 2*a
		print("This equation has two real roots: " + str(root1) + " and " + str(root2))

	#except ValueError:
	#	print("Invalid Entry")

get_roots()