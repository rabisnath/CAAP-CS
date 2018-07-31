months = {
	1: 31,
	2: 28,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31
}

def check_date(m, d, y):
	if m > 12:
		return False
	elif d > months[m]:
		return False
	elif m < 1 or d < 1:
		return False
	else:
		return True

def main():
	date = str(input("Enter a date in the form MM/DD/YYYY\n"))
	try:
		m, d, y = date.split("/")
		m, d, y = int(m), int(d), int(y)
		valid = check_date(m, d, y)
		if valid:
			print("That date is valid")
		else:
			print("That date is NOT valid")
	except ValueError:
		print("Date formatted incorrectly")


main()