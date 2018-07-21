# imports the score class to be used in the leaderboard.
from scores import Score
#import scores.Score
# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		for i in range(self.size):
			self.board.append(Score(" player ", i))

	# prints the leaderboard
	def print_board(self):
		print("High Scores: ")
		print()
		for entry in self.board:
			player = entry.get_name()
			score = entry.get_score()
			print(player + ": ", score)

	# checks if the given score is higher than any of the ones on the lb, then inserts it if it is
	def update(self, score):
		i = 0
		for entry in self.board:
			if (score.get_score() >= entry.get_score()):
				self.board[i].setScore(score.get_score())
			i += 1

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	
	#def insert(self, score, i):
	#	self.board.insert(i, score)
	#	self.board.pop()

def test_leaderboard():
	test_board = Leaderboard()
	test_board.print_board()
	test_board.update(Score("alex", 25))



test_leaderboard()
