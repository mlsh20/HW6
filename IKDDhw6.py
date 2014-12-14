import sys
import numpy as np
from sklearn.metrics import jaccard_similarity_score

inputfile = open("house-votes-84.data", 'r')
cluster1 = file('cluster1.csv', 'w')
cluster2 = file('cluster2.csv', 'w')

pred_id = 1
t = 0
f = 0
true = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 2]

while True:
	line = inputfile.readline()
	if not line: break
	temp = line.split("\n")
	item = temp[0].split(",")
	pred = item[1:]
	i = 0
	while i < len(pred):
		if pred[i] == "y":
			pred[i] = 1
		elif pred[i] == "n":
			pred[i] = 0
		else:
			pred[i] = 2
		i += 1

	if jaccard_similarity_score(true, pred) > 0.3:
		cluster1.write(str(pred_id)+"\n")
		if item[0] == "democrat":
			t += 1
		else:
			f += 1
	else:
		cluster2.write(str(pred_id)+"\n")
		if item[0] == "democrat":
			f += 1
		else:
			t += 1

	pred_id += 1
#print "t:",
#print t
#print "f:",
#print f
inputfile.close()
