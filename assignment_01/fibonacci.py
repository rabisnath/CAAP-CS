def main():
	print("This program will compute the nth term in the fibonacci sequence")
	n = int(input("Please enter a value for n"))
	output = fib(n)
	print("The " + str(n) + "th term in the fibonacci sequence is: " + str(output))

def fib(n):
	a = 0
	b = 1
	for i in range(n-1):
		c = a + b
		a = b
		b = c
	return b

main()