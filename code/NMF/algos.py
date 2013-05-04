import re
import numpy as np
import scipy.sparse as csr
import math
from sklearn import random_projection

filename = "ap/ap.dat"
numWords = 10473
#lowerDimensions = log 40173 * 4 /(0.2*0.2)
lowerDimensions = 500
K= 10
Hbar = []
Hcap = [0]*numWords

f = open(filename, 'r')
for line in f:
	doc = re.findall(r'\w+(?:\'\w+)?',line)
	n = int(doc[0])
	wordcounts = doc[1:]
	Hd = [0] * numWords
	nsqr = (n * (n-1))
	div = math.sqrt(nsqr)

	for i in xrange(0,len(wordcounts),2):
		Hd[int(wordcounts[i])] = (int(wordcounts[i+1])/div)
		Hcap[int(wordcounts[i])] = Hcap[int(wordcounts[i])] + (int(wordcounts[i+1])/nsqr)
	Hbar.append(Hd)

Hbar_sparse = csr.csc_matrix(Hbar).transpose()
Qtemp= Hbar_sparse * Hbar_sparse.transpose()

Hcap_sparse =  csr.csc_matrix(np.diag(Hcap))

Q = Qtemp - Hcap_sparse

#calculating normalized version of sparse matrix
row_sums = np.array(Q.sum(axis=1))[:,0]
row_indices, col_indices = Q.nonzero()
Q.data /= row_sums[row_indices]
#Q is normalized from this point


#Fast anchor words
transformer = random_projection.SparseRandomProjection(lowerDimensions)
D = transformer.fit_transform(Q)



	
