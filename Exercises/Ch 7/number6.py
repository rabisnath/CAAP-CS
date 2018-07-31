def get_speeding_penalty(speed_limit, clocked_speed):
	difference = clocked_speed - speed_limit
	if clocked_speed <= speed_limit:
		print("Speed was legal, no fine")
	elif clocked_speed > 90:
		print("Fine is: " + str(250 + 5*difference) + " dollars.")
	else:
		print("Fine is: " + str(50 + 5*difference) + " dollars.")
		
def main():
	limit = int(input("What is the speed limit on the road in question?"))
	speed = int(input("How fast was the car going?"))
	get_speeding_penalty(limit, speed)

main()