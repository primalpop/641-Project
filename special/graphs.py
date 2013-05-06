import math
import random
import sys
import pdb

"""
Generates a topology with N nodes.
To run: python topgen.py N
Output: python topgen.py 10
"""

""" Degree Variance """

def topology(N, Degree, SD):
	Cords = generate_coordinates(N)
	Neighbours = [[] for i in range(N)]
	for i in range(N):
		Value = Cords[i]
		MyNeighbours = Neighbours[i]
		Max = Degree + random.randrange(-SD, SD)
		el = int(random.random()*10%N)
		V2 = Cords[el]
		OtherNeighbours = Neighbours[el]
		distance = calculate_distance(Value[0], Value[1], V2[0], V2[1])
		if is_neighbour(is_neighbour(distance)):
			if el not in MyNeighbours:
				MyNeighbours.append(el)
				OtherNeighbours.append(i)
			else: continue
			#print MyNeighbours	
			if len(MyNeighbours) > Max: break
			else: continue 

		if MyNeighbours == []:
			rand = int(random.random()*10%N) 	
			index = rand if rand != i else (rand + 1)%N 
			MyNeighbours.append(index)
		Neighbours.append(MyNeighbours)		

	return generate_chain(N, Neighbours)	

	
def generate_chain(N, Neighbours):
	Chain = []
	for i in range(N):
			Nebo = Neighbours[i]
			Element = []
			for j in Nebo:
				Bone = Neighbours[j]
				Other = int(random.random()*10%N)
				Element.append([j+1, Other]) #Pij/2 Lazy 
			Element.append([i+1, int(random.random()*10%N)]) #1 + Pij Lazy 	
			Chain.append(Element)
	return Chain

def calculate_distance(X0,Y0,X,Y):
	return math.sqrt((X-X0)**2 + (Y-Y0)**2)

def generate_coordinates(N):
	return [[random.random(), random.random()] for x in  range(N)]

def is_neighbour(Distance):
	if Distance >= 0.3 or Distance == 0.0:
		return False
	return True


if __name__	== "__main__":
	N = eval(sys.argv[1])
	print topology(N, 5, 5)