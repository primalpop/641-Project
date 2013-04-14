import re
import numpy as np

filename = "ap/ap.dat"
Hbar = []

f = open(filename, 'r')
for line in f:
	doc = re.findall(r'\w+(?:\'\w+)?',line)
	n = int(doc[0])
	wordcounts = doc[1:]
	a = [0] * 10473
	for i in xrange(0,len(wordcounts),2):
		a[int(wordcounts[i])] = int(wordcounts[i+1])
	Hbar.append(a)

Hbarnp = np.array(Hbar)
np.dot(Hbarnp.transpose() , Hbarnp)

