# Joseph Shaffer
# CSE 5243 Programming Assignment 2


import random

i = 0
dict = {}
pruned = {}
overall = {}
sentiments = []
trainSet = []
testSet =[]
validSet = []

with open('amazon_cells_labelled.txt', 'r') as file:
	for line in file:
		dict1 = {}
		for word in line.split():
			if word != '1' and word != '0':
				if overall.has_key(word):
					overall[word] = overall[word] + 1
				else:
					overall[word] = 1
				if dict1.has_key(word):
					dict1[word] = dict1[word] + 1
				else:
					dict1[word] = 1
			else:
				sentiments.append(word)
		dict[i] = dict1
		i = i + 1	

with open('imdb_labelled.txt', 'r') as file:
	for line in file:
		dict1 = {}
		for word in line.split():
			if word != '1' and word != '0':
				if overall.has_key(word):
					overall[word] = overall[word] + 1
				else:
					overall[word] = 1
				if dict1.has_key(word):
					dict1[word] = dict1[word] + 1
				else:
					dict1[word] = 1
			else:
				sentiments.append(word)
		dict[i] = dict1
		i = i + 1	

with open('yelp_labelled.txt', 'r') as file:
	for line in file:
		dict1 = {}
		for word in line.split():
			if word != '1' and word != '0':
				if overall.has_key(word):
					overall[word] = overall[word] + 1
				else:
					overall[word] = 1
				if dict1.has_key(word):
					dict1[word] = dict1[word] + 1
				else:
					dict1[word] = 1
			else:
				sentiments.append(word)
		dict[i] = dict1
		i = i + 1

def rand(percent):
	totalLines = percent / 100.0 * 3000
	start = random.randrange(0, 3000)
	end = start + totalLines
	percent2 = (100 - percent) / 2
	lines = percent2 / 100.0 * 3000
	if end >= 3000:
		end = end - 3000
		end2 = end + lines
		for x in range(start, 3000):
			trainSet.append(x)
		for x in range(0, int(end)):
			trainSet.append(x)
		for x in range(int(end), int(end2)):
			testSet.append(x)
		for x in range(int(end2), start):
			validSet.append(x)
	else:
		for x in range(start, int(end)):
			trainSet.append(x)
		end2 = end + lines
		if end2 >= 3000:
			end2 = end2 - 3000
			for x in range(int(end), 3000):
				testSet.append(x)
			for x in range(0, int(end2)):
				testSet.append(x)
			for x in range(int(end2), start):
				validSet.append(x)
		else:
			for x in range(int(end), int(end2)):
				testSet.append(x)
			end3 = end2 + lines
			if end3 >= 3000:
				end3 = end3 - 3000
				for x in range(int(end2), 3000):
					validSet.append(x)
				for x in range(0, start):
					validSet.append(x)
			else: 
				for x in range(int(end2), start):
					validSet.append(x)
	print trainSet
	print testSet
	print validSet
	





rand(60)




