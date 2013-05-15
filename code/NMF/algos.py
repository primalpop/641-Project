import re
import numpy as np
import scipy.sparse as csr
import math
from sklearn import random_projection
from projections import *
import linecache
def NMFTopicmodelling(K):
	filename = "ap/ap.dat"
	numWords = 10473
	#lowerDimensions = log 40173 * 4 /(0.2*0.2)
	lowerDimensions = 500
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

	maxindex = np.argmax((D.multiply(D)).sum(1))
	S = np.matrix(D[maxindex].todense())
	Sdash = [maxindex]

	for i in xrange(1,K):
		projectionMatrix = calcOrthogonalProjectionMatrix(S.T)
		maxValue = float("-inf")
		for j in xrange(1,D.shape[0]):
			orthogonalComponent= (projectionMatrix * D[j].T)
			distance = np.sum(np.square(orthogonalComponent))
			if maxValue < distance :
				maxValue = distance
				maxindex = j
		print str(i)
		S = np.vstack([S,D[maxindex].todense()])
		Sdash.append(maxindex)


	for i in xrange(1,K):
		escapedS =  np.vstack( [S[0:i][:],S[i+1:K][:]])
		projectionMatrix = calcOrthogonalProjectionMatrix(escapedS.T)
		maxValue = float("-inf")
		for j in xrange(1,D.shape[0]):
			orthogonalComponent= (projectionMatrix * D[j].T)
			distance = np.sum(np.square(orthogonalComponent))
			if maxValue < distance :
				maxValue = distance
				maxindex = j
		print str(i)
		S = np.vstack([S[0:i][:],D[maxindex].todense(),S[i+1:K][:]])
		Sdash = Sdash[0:i] + [maxindex] + Sdash[i+1:K]

	for i in Sdash:
		print linecache.getline("ap/vocab.txt",i+1)

for i in xrange(1,10):
	NMFTopicmodelling(i)