"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
	# create dictionary of counts of elements in dice list
	d = dict({(i, dice.count(i)) for i in dice})
	
	# checking YACHT
	if category == 'YACHT':
		return 50 if len(d)==1 else 0

	# checking ONES
	if category == 'ONES':
		return d[1] if 1 in d.keys() else 0

	# checking TWOS
	if category == 'TWOS':
		return 2*d[2] if 2 in d.keys() else 0

	# checking THREES
	if category == 'THREES':
		return 3*d[3] if 3 in d.keys() else 0

	# checking FOURS
	if category == 'FOURS':
		return 4*d[4] if 4 in d.keys() else 0

	# checking FIVES
	if category == 'FIVES':
		return 5*d[5] if 5 in d.keys() else 0

	# checking SIXES
	if category == 'SIXES':
		return 6*d[6] if 6 in d.keys() else 0

	# checking FULL_HOUSE
	if category == 'FULL_HOUSE':
		return sum(dice) if (len(d)==2 and 2 in d.values() and 3 in d.values()) else 0

	# checking FOUR_OF_A_KIND
	if category == 'FOUR_OF_A_KIND':
		if 4 in d.values() or 5 in d.values():
			for i in d.keys():
				if d[i]==4 or d[i]==5:
					k=i
			return 4*k
		else:
			return 0

	# checking LITTLE_STRAIGHT
	if category == 'LITTLE_STRAIGHT':
		return 30 if (len(d)==5 and 1 in d.keys() and 6 not in d.keys()) else 0

	# checking BIG_STRAIGHT
	if category == 'BIG_STRAIGHT':
		return 30 if (len(d)==5 and 6 in d.keys() and 1 not in d.keys()) else 0

	# checking CHOICE
	if category == 'CHOICE':
		return sum(dice)

























