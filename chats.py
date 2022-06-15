from parser import parse
import sys
import math
import random

# Increasing this will gain more similarity with the original text but will also increase time
PREDICTION_DEPTH = 5

# The generated statement will be atleast 95% the length of the original
LENGTH_MIN_PERCENT = 0.95

PUNCT = "!?.,;:"

def getWordSets(words):
	wordSets = []

	for size in range(PREDICTION_DEPTH, 0, -1):
		wordSet = [size]
		for i in range(len(words)-size+1):
			current = words[i:i+size]

			# I consider this punctuation as thought ending and wanted to ignore word sets that contain them in the middle
			if "." not in current[1:-1] and "!" not in current[1:-1] and "?" not in current[1:-1]:
				if len(current) > 1 or current[0] not in ".?!;,:":
					wordSet += [current]

		if wordSet != [size]:
			wordSets += [wordSet]

	return wordSets

def getNextWord(recent, wordSets):
	choices = []

	# Case for starting a new sentance
	if recent == []:
		for size in wordSets[-2:]:
			for ws in size[1:]:
				if ws[0] in ".?!":
					choices += [ws]
		choices += [wordSets[-1][1]]
		return random.choice(choices)[-1]


	for size in wordSets[PREDICTION_DEPTH - len(recent)-1:]:
		s = size[0]
		for ws in size[1:]:
			if recent == ws[:-1]:
				choices += [ws]
		recent = recent[1:]
		if choices != []:
			return random.choice(choices)[-1]



def chats(words, length):
	recentWords = []
	statement = ""
	wordSets = getWordSets(words)
	while len(statement) < length or statement[-2:] not in ". ? ! ":
		new = getNextWord(recentWords, wordSets)
		if recentWords == []:
			new = new[0].upper() + new[1:]
		if new in PUNCT:
			statement = statement[:-1] + new + " "
			if new in ".?!":
				recentWords = []
			else:
				recentWords += [new]
				if len(recentWords) >= PREDICTION_DEPTH:
					recentWords = recentWords[1:]
		else:
			statement += new + " "
			recentWords += [new]
			if len(recentWords) >= PREDICTION_DEPTH:
				recentWords = recentWords[1:]

	return statement


		

		


if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise Exception("Incorrect number of arguments")

	filename = sys.argv[1]
	if filename[-4:] != ".txt":
		raise Exception('Must input a ".txt" file')
	
	with open(filename) as file:
		txt = str(file.read())

		length = math.floor(len(txt) * LENGTH_MIN_PERCENT)
		
		print(chats(parse(txt), length))
		
	file.close()