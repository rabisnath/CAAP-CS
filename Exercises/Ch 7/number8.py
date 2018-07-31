def check_eligibility(age, years_cit):
	if age >= 30 and years_cit >= 9:
		print("This person is eligible to be a US Senator or Representative")
	elif age >= 25 and years_cit >= 7:
		print("This person is eligible to be a US Representative")
	else:
		print("This person is not eligible to be a Senator or a Representative")

def main():
	age = int(input("How old is this person?"))
	yearsofcit = int(input("How long has this person been a citizen?"))
	check_eligibility(age, yearsofcit)

main()