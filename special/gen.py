import math
import random
import sys
import primalgorithm

"""
Generates a graph with N vertices and edge costs.
To run: python topgen.py N
Output: python topgen.py 5
[[0, 0, 3, 0, 4], [0, 0, 0, 2, 2], [1, 0, 0, 0, 4], [0, 5, 0, 0, 0], [2, 1, 5, 0, 0]]
"""

def topology(N, threshold):
	Cords = generate_coordinates(N)
	graph = [[0 for i in range(N)] for j in range(N)]
	for i in range(N):
		Value = Cords[i]
		for j in range(N):
			V2 = Cords[j]
			distance = calculate_distance(Value[0], Value[1], V2[0], V2[1])
			if is_neighbour(distance,threshold):
				graph[i][j] = int(distance * 100)
				graph[j][i] = int(distance * 100)	
			else: continue
		if set(graph[i]) == set([0]) :
			rand = int(random.random()*10%N) 	
			index = rand if rand != i else (rand + 1)%N 
			graph[i][index] = rand
			graph[index][i] = rand			

	return graph	

def calculate_distance(X0,Y0,X,Y):
	return math.sqrt((X-X0)**2 + (Y-Y0)**2)

def generate_coordinates(N):
	return [[random.random(), random.random()] for x in  range(N)]

def is_neighbour(Distance, threshold=0.4):
	if Distance >= 0.4 or Distance == 0.0:
		return False
	return True

import numpy
import time
import pylab as pl

if __name__	== "__main__":
	timings_threshold = []
	N = 250 #No of vertices
	V = range(N)
	timings_threshold = []
	range_of_threshold = numpy.linspace(0.1, 0.95, 20)
	for nt in range_of_threshold:
	    start = time.time()
	    A = topology(N,nt)        
	    P = primalgorithm.prim(V, A, 0)
	    end = time.time()
	    t = end - start
	    timings_threshold.append(t)
	    print t
	    #print P

	#print timings_threshold

	#plotting the results		
	pl.plot(range_of_threshold, timings_threshold)	
	pl.title(" Analysis of Graph density effect on MST Algorithms ")
	pl.ylabel("Time")
	pl.xlabel("Graph Density")
	pl.show()	    