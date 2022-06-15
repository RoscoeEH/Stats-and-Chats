from parser import parse
import sys

PUNCT = "!?.,;:"

def fixOrder(i, usage):
	while i > 0 and usage[i][1] > usage[i-1][1]:
		temp = usage[i]
		usage[i] = usage[i-1]
		usage[i-1] = temp
		i -= 1

def findIncrement(string, usage):
	for i, use in enumerate(usage):
		if use[0] == string.lower():
			use[1] += 1
			fixOrder(i, usage)
			return False
	return True


def stats(strings):
	usage = []
	for string in strings:
		if string not in PUNCT:
			add = findIncrement(string, usage)
			if add == True:
				usage += [[string.lower(), 1]]
	return usage


if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise Exception("Incorrect number of arguments")

	filename = sys.argv[1]
	if filename[-4:] != ".txt":
		raise Exception('Must input a ".txt" file')
	
	with open(filename) as file:
		txt = parse(str(file.read()))
		output = stats(txt)
		for word in output:
			print(f"{word[0]} : {word[1]}")
	file.close()