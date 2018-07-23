# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class template(Scene):

	name = ""

	def enter(self):
		print("")
		print("")
		return self.action()

	def action(self):
		print("What do you do?")
		print("1: ")
		print("2: ")
		print("3: ")
		choice = input("> ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print("")
			print("")
			return self.exit_scene("")
		elif int(choice) == 2:
			print("")
			print("")
			return self.exit_scene("")
		elif int(choice) == 3:
			print("")
			print("")
			return self.exit_scene("")
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class RoundOne(Scene):

	name = "round_one"

	def enter(self):
		print("You are a varsity lincoln douglas debater. Today is April 28th, 2018, the first day of rounds at the Tournament of Champions.")
		print("If you don't know what that means, type '?', if you're good, enter any other input besides ':q', that's how you quit the game.")
		choice = input("> ")
		if choice == '?':
			print("Lincoln douglas debate is a one-on-one debate format created by the National Speech and Debate Association in which \n highschool students discuss various policy topics with a focus on philosophy and critical theory.")
			print("The Tournament of Champions is the most important tournament of most people's careers, if they're among the lucky few who ever even make it there.")
			print("A round of debate consists of the two debaters taking turns making speeches, the speech order is: 1AC, 1NC, 1AR, 2NR, 2AR")
			print("Where A indicates a speech made by the affirmative debater, N by the negative debater, C indicates that the speech is constructive, while R stands for rebuttal")
			print("A tournament ususally consists of a set of prelim rounds, and then a set of out rounds, that work like the regular season and the playoffs of american football respectively")
			print("Good luck!")
		else:
			print("You're feeling well rested after sleeping in the finest 2 star hotel Kentucky has to offer.\n You're listening to SATURATION II on full blast on your Apple Earpods when you get the Tabroom alert with your postings. \n You're aff.")
		print()
		return self.action()

	def action(self):
		print("What do you do?")
		print("1: Read the judge's paradigm")
		print("2: Look for your opp's school on the disclosure wiki")
		print("3: Do some last minute speed drills")
		choice = input("> ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print("Your judge is a first year out pf debater who says he weighs substance before T")
			print("You go all in on substance in the 1AR even though the neg strat was 5 off. Miraculously, you pick up.")
			return self.exit_scene("round_five")
		elif int(choice) == 2:
			print("Your opponent is a lone wolf who doesn't believe in disclosure, they're not on the wiki. You somehow end up staring at a picture of Jimmy Chen for 20 minutes.")
			print("They read Wilderson, you didn't flow the argument, attempt to perm the alt in the 1AR, and drop the 6 'perm fails' analyics they read in the NC. You drop.")
			return self.exit_scene("death")
		elif int(choice) == 3:
			print("You spread the lyrics to the most recent Ugly God single 6 times.")
			print("You spread so fast during round that your table tote collapses in the middle of your 1AR due to the force of your breath.\n You spend 1 minute trying to put it back together and drop the K. You drop.")
			return self.exit_scene("death")
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class RoundFive(Scene):

	name = "round_five"

	def enter(self):
		print("Fast Forward. You're 3-1, heading into round five, you haven't eaten anything due to stress but you're staying hydrated. You feel good.")
		print("Your get your postings, you're hitting Lake Highland's Julia Wu. Your coach, Jack Ave, calls you and spills that she's running the Deleuze aff she broke with at Harvard.")
		return self.action()

	def action(self):
		print("What do you do in the 1NC?")
		print("1: Read T")
		print("2: Read Baudrillard")
		print("3: Read the 50 states CP and a politics DA")
		choice = input("> ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print("You spread through every single shell in your dropbox, but forget to read the RVIs bad analyics your coach gave you.")
			print("Two judges vote for her off the RVI, the other thinks K comes before T and signed their ballot after the 1NC.")
			return self.exit_scene("death")
		elif int(choice) == 2:
			print("You read Baudrillard in the 1NC, she says the aff solves the K in the 1AR. In the 2NR you pop off, \nexplaining that Baudrillard's theory of pure negation demands a neg ballot.")
			print("You pick up on a 2-1.")
			return self.exit_scene("double_octos")
		elif int(choice) == 3:
			print("You read your CP, she reads A-Spec in the 1AR, you don't even know what that is and lose the argument.")
			print("One judge drops you out of sheer hatred of the 50 states CP, one drops you on A-Spec, and the other votes on something Julia said about critical education in the 1AC.")
			return self.exit_scene("death")
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class DoubleOctos(Scene):

	name = "double_octos"

	def enter(self):
		print("Fast forward again. You went 6-1 and broke to double octofinals! Your only loss was to a debate drills kid that reads skep every round on every topic.")
		print("Your teammates didn't break are going to follow you into your next round. You notice a tear of joy roll down Jack's face.")
		print("Postings: You're hitting Greenhill BZ; you're aff. You read the Mass Incarceration AC you spent 23 hours cutting over christmas break. \n The neg order is: the Cap K, a DA and some blippy arguments about presumption")
		return self.action()

	def action(self):
		print("You only have time to cover two arguments in the 1AR, what do you do? (Besides extending the aff)")
		print("1: Delink from the K then address the presumption arguments")
		print("2: Try to perm the alt and then respond to the DA")
		print("3: Go for T and presumption")
		choice = input("> ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print("You try your best to delink from the K, but you can't work your way around the fact that captialism is the root cause of the prison industrial complex.")
			print("You lose on a 5-0.")
			return self.exit_scene("death")
		elif int(choice) == 2:
			print("They drop the DA and go all in on the K in the 2NR. Lucky for you the judges end up giving you access to the perm")
			print("You pick up on a 4-1.")
			return self.exit_scene("semis")
		elif int(choice) == 3:
			print("You read a tshell and try and beat back the presumption arguments, but Brian goes all in on the K in the 2NR, it's not pretty.")
			print("You drop on a 5-0. Don't drop the K next time.")
			return self.exit_scene("death")
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Semis(Scene):

	name = "semis"

	def enter(self):
		print("You made it to semis!! Your posse is exhausted but spirits are still high.")
		print("*Ding* Santa Monica RE. You're Neg. Pressure's on.")
		return self.action()

	def action(self):
		print("He reads a Kant aff, like usual, how do you respond in the 1NC?")
		print("1: Read 3 minutes of Kant indicts")
		print("2: Read 3 minutes of Util good")
		print("3: Run Cap")
		choice = input("> ")

		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print("You spend 180 seconds explaining that Kant is ontologically equivalent to the link to anti-blackness. \nThe 1AR explain that those indicts don't matter because the author is separate from the body of work.")
			print("You drop on a 5-2.")
			return self.exit_scene("death")
		elif int(choice) == 2:
			print("You spend almost half your speech reciting your ode to util. The 1AR is 2 minutes of Bostrom and then substance. \n You don't really know anything about Kant or Bostrom.")
			print("You lose on a 7-0.")
			return self.exit_scene("death")
		elif int(choice) == 3:
			print("It's a close round, you end up winning on some 2NR analytics about the self-perpetuating nature of captialism.")
			print("You're going to finals!")
			return self.exit_scene("finals")
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Finals(Scene):

	name = "finals"

	def enter(self):
		print()
		print()
		print("This is it. TOC finals. You dig through your dropbox to find the thank you speech you wrote back when you were a sophomore dreaming about this moment.")
		print()
		print("You're aff against... ")
		print()
		print("Oh my god, is that...")
		print()
		print("James Chen?! In LD!?")
		print()
		print("The god-king of Public Forum debate, Jimmy Chen stands up to give the 1NC.")
		print()
		print("He opens his mouth and the room is consumed in a swirling vortex of argumentation, his voice sounds like it's from a different dimension: forbidden, ancient")
		print()
		print("The order is: ")
		print("A Biopower K, A Nietzsche K, Psychoanalysis, A PTX DA, 8 Pages of Econ Impacts and 6 T Shells. God help you.")
		return self.action()

	def action(self):
		print()
		print("Your speech order is going to be: The K's, Psychoanalysis, The DA, Econ, and T.")
		print("You have 100 hp, Jimmy has 200 hp, when an argument is won, the loser will lose 40 health.")

		arguments = ["The Kritiks", "Psychoanalysis", "The DA", "Econ", "T"]

		wrong_answers = [3, 2, 3, 3, 2]

		options = [
			["1: Lable reading Nietzsche and Biopower as a performative contradiction", "2: Indict the use of philosophy like Nietzsche as securitizing the debate space, linking to Biopower", "3: Read anti-blackness"],
			["1: Read 5 blippy delinks", "2: Read Freud indicts", "3: Perm the alt"],
			["1: Ignore this layer of the debate", "2: Read delinks", "3: Read a turn"],
			["1: Ignore this layer of the debate", "2: Read delinks", "3: Read turns"],
			["1: Go for an RVI", "2: Contest the violation", "3: Contest the standards"],
		]

		playerHP = 100
		jamesHP = 200

		for i in range(5):
			print()
			print("You have: ", playerHP, "health, Jimmy has: ", jamesHP, "health")
			print()
			print(str(i+1)+"th up is: " + arguments[i])
			print("What do you do: ")
			for option in options[i]:
				print(option)
			choice = input("> ")

			if choice == ':q':
				return self.exit_scene(choice)
			try:
				choice = int(choice)
			except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)			

			if int(choice) == wrong_answers[i]:
				print("You feel your stomach drop as you realize that you made the wrong decision. \nJimmy cracks a smile as the speaker points wash over him")
				playerHP -= 40
			else:
				print("Jimmy's smug look falters, one of the judges nods; you've chipped away at the titan.")
				jamesHP -= 40

			if playerHP < 0:
				print("One mistake too many, better luck next time")
				return self.exit_scene("death")

			if jamesHP < 0:
				print("You did it! You did the undoable, you beat Jimmy Chen!")
				return self.exit_scene("finished")

		if jamesHP < playerHP:
			print("You did it! You did the undoable, you beat Jimmy Chen!")
			return self.exit_scene("finished")
		else:
			print("One mistake too many, better luck next time")
			return self.exit_scene("death")


	def exit_scene(self, outcome):
		return outcome