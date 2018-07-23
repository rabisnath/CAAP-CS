# importing package to be able to run the tests
from nose.tools import *
# Here you should import all the modules/classes you want to test
import game
import game.scores
import game.leaderboard


# define a function like these for each class/module you test.
def test_scores():
	test_score = Score('alex', 8)
	if (test_score.get_name() != 'alex'):
		raise Valuerror ('Not expected value')

def test_leaderboard():
	testBoard = Leaderboard()
	print(testBoard)
# etc...