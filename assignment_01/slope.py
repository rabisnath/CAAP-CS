def main():
	n = int(input("How many numbers would you like to sum?"))
	numbers = []
	count = 0
	while (count < n):
		numbers.append(float(input("Enter the next number")))
		count += 1
	total = sum(numbers)
	print("The sum of those numbers is: " + str(total))

main()