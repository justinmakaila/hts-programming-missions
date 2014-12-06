import sys

wordsListPath = "../Downloads/wordlist.txt"
alphabet = 'qwertyuiopasdfghjklzxcvbnm:()1234567890;'

def empty_frequencies():
	freq = {}
	for i in range(0, len(alphabet)):
		freq[alphabet[i]] = 0

	return freq

def frequencies(string):
	freq = empty_frequencies()

	for i in range(0, len(string)):
		freq[string[i]] += 1

	return freq

def matcher(word):
	wordFrequencies = frequencies(word)

	def match(aWord):
		frequency = frequencies(aWord)

		c = ''
		for i in range(0, len(alphabet)):
			c = alphabet[i]

			if wordFrequencies[c] != frequency[c]:
				return False

		return True

	return match

def main(word, dict):
	mf = matcher(word)
	matches = []

	for i in range(0, len(dict)):
		if mf(dict[i]):
			matches.append(dict[i])

	return matches

# Read the words list into a list
wordsList = [line.strip() for line in open(wordsListPath, "r")]

firstArgument = sys.argv[1]
scrambledWords = firstArgument.split('\n')

result = ""
for word in scrambledWords:
	result += main(word, wordsList)[0] + ","

print result

