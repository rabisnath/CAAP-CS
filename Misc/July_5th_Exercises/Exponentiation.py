def exp(base, exp):
	temp = 1.00
	count = 0
	while (count < exp):
		temp *= base
		count += 1
	return temp

def main():
	b = int(input("Base?"))
	x = int(input("Exponent?"))
	output = exp(b, x)
	print ("result is: ", output)

main()