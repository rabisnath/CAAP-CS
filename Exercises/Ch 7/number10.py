def get_easter(year):
	a = year % 19
	b = year % 4
	c = year % 7
	d = (19*a + 24) % 30
	e = (2*b + 4*c + 6*d + 5) % 7

	exceptions = [1954, 1981, 2049, 2076]

	easter_month = "March"
	easter_date = 22 + d + e

	if year in exceptions:
		easter_date -= 7

	if easter_date > 31:
		easter_month = "April"
		easter_date -= 31

	return easter_month, easter_date

def main():
	yr = int(input("What year are you looking at?"))
	month, date = get_easter(yr)
	print("Easter will be on " + month + " " + str(date) + " that year")

main()