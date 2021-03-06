# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0 #number of moves the player has made so far
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	leaderboard.update(score)
	if (won):
		print("\nYou Won!")
	else:
		print ("\nGame Over. Better luck next time.")
	leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		print ("Welcome to my game! To quit enter :q at any time.") # raise ValueError ('todo')
		name = input("\nOkay Let's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ':q'):
			exit(1)
		a_map = Map('round_one') # raise ValueError ('todo')
		a_game = Engine(a_map)
		moves = a_game.play()
		game_over(a_game.won())

play_game()