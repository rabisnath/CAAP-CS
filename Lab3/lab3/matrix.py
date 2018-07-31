from random import randint

# takes the number of rows and columns and makes a matrix of those dimensions
def make_matrix(r, c, rand): #the rand parameter allows generation of randomly populated matricies for testing
	matrix = []
	for i in range(r): # making a list for each row
		row = []
		for j in range(c): # filling the rows with 0s
			if rand:
				row.append(randint(0, 5))
			else:
				row.append(0)
		matrix.append(row)
	return matrix

#takes a matrix and returns the Nth column (zero indexed) in a list
def getColumn(matrix, n):
	column = []
	for row in matrix:
		column.append(row[n])
	return column

#returns the dot product of two vectors
def dotproduct(a, b):
	output = 0
	for i in range(len(a)):
		output += a[i] * b[i]
	return output

# takes two matrices and multiplies them returnin the resulting matrix
def matrixmult(a,b):
	rowsOfA = len(a) #these four lines get the dimensions of the two matricies
	colsOfA = len(a[0])
	rowsOfB = len(b)
	colsOfB = len(b[0])

	if colsOfA != rowsOfB: #making sure dimensions are valid
		raise ValueError("Invalid Matrix Dimensions")

	c = make_matrix(rowsOfA, colsOfB, False) #generates an empty matrix for c

	for i in range(len(c)):
		for j in range(len(c[0])):
			c[i][j] = dotproduct(a[i], getColumn(b, j)) #carrying out the multiplication, filling in each cell in c

	return c



# prints the given matrix, mostly for testing purposes
def print_matrix(m):
	for row in m:
		print(row)

# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation(state_matrix, transition_matrix, trials):
	clean_state_matrix = state_matrix

	print("Running simulation " + str(trials) + " times")

	total_moves = 0
	
	for i in range(trials):
		moves = 0
		percent_won = 0
		while percent_won < 0.99:
			#print_matrix(state_matrix)
			#print_matrix(transition_matrix)
			state_matrix = matrixmult(state_matrix, transition_matrix)
			moves += 1
			percent_won = float(state_matrix[0][len(state_matrix[0])-1])
		total_moves += moves
		print("Trial #" + str(i) + ": " + str(moves) + " moves")
		state_matrix = clean_state_matrix


		
	
	avg = float(total_moves) / float(trials)

	print("Average number of moves required was: " + str(avg))

	log = open("markov_test_results.txt", "a+")
	log.write("\nRan simulation " + str(trials) + " times, Average number of moves required was: " + str(avg))
	log.close()

	return avg

#first markov sim function returns the number of moves it takes to win,
#this one returns the probability of the game being over on a given turn
def markov_simulation_bymove(state_matrix, transition_matrix, turn):
	for i in range(turn):
		state_matrix = matrixmult(state_matrix, transition_matrix)
	percent_won = float(state_matrix[0][len(state_matrix[0])-1])

	print("Chance of winning on turn " + str(turn) + " is " + str(percent_won))

	log = open("markov_test_results.txt", "a+")
	log.write("Chance of winning on turn " + str(turn) + " is " + str(percent_won))
	log.close()

	return percent_won

def testing_bymove(state_matrix, transition_matrix, n, increment):
	for i in range(0, n, increment):
		markov_simulation_bymove(state_matrix, transition_matrix, i)


#def test():
	#testing matrix mult
	#A = make_matrix(2, 3, True)
	#B = make_matrix(3, 2, True)
	#C = matrixmult(A, B)
	#print("A: ")
	#print_matrix(A)
	#print("B: ")
	#print_matrix(B)
	#print("C: ")
	#print_matrix(C)

	#testing markov sim


#test()