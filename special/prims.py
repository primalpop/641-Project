from collections import defaultdict
from heapq import *
import gen

def prim( nodes, edges ):
    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )


    mst = []
    used = set( nodes[ 0 ] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )


    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )


            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    return mst

A = gen.topology(1000, 0.4)        
N = [str(x) for x in list(xrange(len(A)))]

p = []

for i in xrange(1,len(A)):
  for j in xrange(1,i):
    if A[i][j] != 0:
      p.append((str(i),str(j),A[i][j]))

print len(p)

prim(N, p)