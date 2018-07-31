credit_levels = {
	"Freshman": 7,
	"Sophomore": 16,
	"Junior": 26,
}

def classify_student(credits):
	classification = ""

	for level in credit_levels:
		if credits < credit_levels[level]:
			classification = level
			break

	if classification == "":
		classification = "Senior"

	return classification

def main():
	creds = int(input("How many credits does the student you want to classify have?"))
	level = classify_student(creds)
	print("A student with " + str(creds) + " credits would be a " + level)

main()