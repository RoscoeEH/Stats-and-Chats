
# These constants tell make up the acceptable characters
PUNCT = "!?.,;:"
ALPHA = "qwertyuiopasdfghjklzxcvbnm1234567890'-$"


# This function turns the text into a list containing all words and punctuation.
# I am aware that the .split() method exists but I chose to do this to sort for punctuation and unrecognized characters.
def parse(txt):
	txt = txt.lower()
	words = [txt[0]]
	space = False
	for char in txt[1:]:
		if char in " \n":
			space = True
		elif char in PUNCT:
			words += [char]
		elif char in ALPHA:
			if space == True:
				words += [char]
				space = False
			else:
				words[-1] += char
		else:
			# Unrecognized character
			raise Exception(f'Unexpected character: "{char}".')
	return words

