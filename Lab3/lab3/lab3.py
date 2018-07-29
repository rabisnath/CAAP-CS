# Alex Bisnath
# Lab 3

import random
import math
from random import randint
import matrix as m

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14: 6}

specialTileDensity = 0.4 # probability of a given square having a chute/ladder
variance = 12 # max distance a chute/ladder can move the player

# Rolls a die of six sides and returns the result
def roll_die():
	return randint(1, 6)

# makes a game (just a list) of the given dimensions
# code marked with #### should be toggled to change from using the preset array of chutes and ladders to generating them randomly
def makeGame(r, c):
	global chutes_ladders####
	gameBoard = []
	for i in range(r): #making a dicitonary to represent each row
		row = {}
		for j in range(c): #filling in each row with kv pairs representing each space on the board. Most spaces are like 5:5, ladders look like 7:20 etc
			index = i*c + j + 1
			####if random.uniform(0, 1) < specialTileDensity: #this decides if a given cell will be a chute/ladder
			####	row[index] = index + int(random.uniform(-1, 1)*min(variance, index))
			if index in chutes_ladders:####
				row[index] = chutes_ladders[index]####
			else:
				row[index] = index
		gameBoard.append(row)
	return gameBoard

def resolve(board, index):
	width = len(board[0])
	row = math.floor((index - 1) / width) 
	return board[row][index]

# checks if given square is a chutes or ladders
def is_chutes_ladders(gameBoard, index):
	width = len(gameBoard[0])
	row = (index - 1) // width 
	if gameBoard[row][index] > index:
		return 1 #this indicates ladder
	elif gameBoard[row][index] < index: 
		return -1 #this indicates chute
	else:
		return 0 #this indicates a regular tile

#converts a list in the form [2, 2, 3] to a dict in the form {2: 2, 3: 1}
def convert_to_freq(array):
	output = {}
	for item in array:
		if item in output:
			output[item] += 1
		else:
			output[item] = 1
	return output

#based on https://www.geeksforgeeks.org/bubble-sort/
def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

#returns a list of possible states on a given board
def get_possible_states(board):
	height = len(board)
	width = len(board[0])
	size = height*width
	possibleStates = [] #generating a list of indicies where it is possible for a player to end their turn
	for i in range(size):
		row = i // width
		if not (board[row][i+1] in possibleStates):
			possibleStates.append(board[row][i+1])

	bubble_sort(possibleStates)	#sorts the list of possible states		

	return possibleStates

#EXTRA CREDIT
#generates the transition matrix for a given board
def get_transition_matrix(board):
	height = len(board)
	width = len(board[0])
	size = height*width

	possibleStates = get_possible_states(board)

	#print(possibleStates)

	transitionMatrix = []

	for state in possibleStates:
		destinations = []
		probabilities = []

		for landingTile in range(state + 1, state + 7):
			destinations.append(resolve(board, min(landingTile, size)))
			
		destinations = convert_to_freq(destinations)

		for dest in possibleStates:
			if dest in destinations:
				probabilities.append(destinations[dest] / 6)
			else:
				probabilities.append(0)

		transitionMatrix.append(probabilities)

#	current_row = 0
#	for row in board: #looping through the rows of the board
#		for i in range(len(row)+1): #looping through the cells in a row
#			index = i + current_row*width #i is the position of a cell in a row, need the second term to add prev rows
#			if not (index in possibleStates): #makes it so the vertical axis only contains possible states
#				continue
#			destinations = [] #an array of the states cell i links to
#			probabilities = [] #the row of the transition matrix corresponding to this cell
#			for landingTile in range(i + 1, i + 7): #looping through the cells one die roll away from i
#				destinations.append(resolve(board, min(landingTile + width*current_row, size))) #populates destinations w end of turn positions
#			destinations = convert_to_freq(destinations) #converts from [1, 2, 7, 7] to {1: 1, 2: 1, 7: 2}
#			for dest in possibleStates: #populating the probabilities array
#				if dest in destinations:
#					probabilities.append(destinations[dest] / 6)
#				else:
#					probabilities.append(0)
#			transitionMatrix.append(probabilities)
#		current_row += 1

	return transitionMatrix

#generates initial state matrix for a given board
def get_init_state_matrix(board):
	states = get_possible_states(board)
	state_matrix = [[1]]
	for i in range(len(states)-1):
		state_matrix[0].append(0)
	return state_matrix


# function to make and play a game
def play_game(numPlayers, r, c):
	numRows = r
	numCols = c
	gameBoard = makeGame(numRows, numCols)

	#numPlayers = int(input("How many people are playing? Type 0 to watch the computer play."))
	if numPlayers == 0:
		mode = 'pc'
	else:
		mode = 'user'

	gameState = [{}] # This should be a list of dictionaries of each player's state
	for i in range(max(numPlayers, 1)): #initiallizing the players on the first tile, the max handles the case where the pc is playing
		gameState[0][i] = 1 

	gameOver = False

	if mode == 'user':
		turnNumber = 1
		while gameOver == False:
			miniHistory = {} #this contains the data for what happened to each play this turn, exported to the gameState array at the end of the for loop
			for player in range(numPlayers):
				print("Player " + str(player + 1) + ": it's your turn!") #prompting the user to roll the die
				print("Type 'q' to quit, enter anything else to roll the die.")
				choice = input("> ")
				if choice == 'q':
					return
				else:
					roll = roll_die()
					oldPosition = gameState[turnNumber - 1][player] # temp position exists so we can tell the player if they hit a ladder/chute
					tempPosition = gameState[turnNumber - 1][player] + roll
					print("You rolled a " + str(roll) + "!")

					if tempPosition >= numRows * numCols: # this intejecting if checks if a player wins
						print("You won the game! It took " + str(len(gameState)) + " moves")
						gameOver = True
						miniHistory[player] = tempPosition
						break

					newPosition = resolve(gameBoard, tempPosition) #resolve is what moves a player up a ladder/down a chute
					miniHistory[player] = newPosition
					if is_chutes_ladders(gameBoard, tempPosition) < 0:
						print("Oh no! You fell down a chute!")
					elif is_chutes_ladders(gameBoard, tempPosition) > 0:
						print("Yes! You found a ladder!")
					print("You moved from " + str(oldPosition) + " to " + str(newPosition))

			gameState.append(miniHistory)
			turnNumber += 1
	else:
		turnNumber = 1
		while gameOver == False:
			roll = roll_die()
			oldPosition = gameState[turnNumber - 1][0]
			tempPosition = gameState[turnNumber - 1][0] + roll

			if tempPosition >= numRows * numCols:
				gameOver = True
				gameState.append({0: tempPosition})
				#print("Game finished in " + str(len(gameState)) + " moves")
				break

			newPosition = resolve(gameBoard, tempPosition)
			gameState.append({0: newPosition})
			turnNumber += 1


	return len(gameState)

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
def simulate_game(n, r, c):
	print("Running simulation " + str(n) + " times")
	totalMoves = 0
	for i in range(n):
		trialMoves = play_game(0, r, c)
		totalMoves += trialMoves
	average = float(totalMoves) / float(n)
	print("Average number of moves required was: " + str(average))

	log = open("naiveTestResults.txt", "a")
	log.write("\nRan simulation " + str(n) + " times, Average number of moves required was: " + str(average))
	log.close()

	return average
	
def print_transition_matrix(m):
	printableVersion = []

	for row in m:
		exportRow = []
		for entry in row:
			if entry == 1.0/6.0:
				exportRow.append("1/6")
			elif entry == 1.0/3.0:
				exportRow.append("1/3")
			elif entry == 1.0/2.0:
				exportRow.append("1/2")
			elif entry == 2.0/3.0:
				exportRow.append("2/3")
			elif entry == 5.0/6.0:
				exportRow.append("5/6")
			elif entry == 1:
				exportRow.append("1")
			else:
				exportRow.append("0/0")
		printableVersion.append(exportRow)

	print()
	for row in printableVersion:
		print(row)	
		print()

def test():
	#numPlayers = int(input("How many people are playing? Type 0 to watch the computer play."))
	#r = int(input("How many rows"))
	#c = int(input("How many columns"))
	#play_game(numPlayers, r, c)

	#trials = int(input("How many trials would you like to do?"))
	#simulate_game(trials, 6, 6)

	#EXTRA CREDIT: Can test on any sized game board by giving makeGame() different parameters
	testBoard = makeGame(8, 8)
	testTransMatrix = get_transition_matrix(testBoard)
	#print_transition_matrix(testTransMatrix)
	testStateMatrix = get_init_state_matrix(testBoard)
	#print(get_possible_states(testBoard))
	#m.print_matrix(testStateMatrix)
	
	#m.markov_simulation(testStateMatrix, testTransMatrix, 10)

	#m.markov_simulation_bymove(testStateMatrix, testTransMatrix, 1000)

	m.testing_bymove(testStateMatrix, testTransMatrix, 20, 1)




test()