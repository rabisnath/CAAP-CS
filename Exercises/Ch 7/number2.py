grade_dict = {
	"A": 5,
	"B": 4,
	"C": 3,
	"D": 2
}

def grade_quiz(score):
	letter_grade = ""

	for grade in grade_dict:
		if score == grade_dict[grade]:
			letter_grade = grade

	if letter_grade == "":
		letter_grade = "F"

	return letter_grade

def main():
	score = int(input("What quiz score would you like a grade for?"))
	grade = grade_quiz(score)
	print("That score corresponds to a(n): " + str(grade))

main()