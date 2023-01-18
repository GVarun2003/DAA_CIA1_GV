The Question. 
solve the directed, negative weighted graph, using the matrix

[[0,4,2,0,0],[0,0,3,2,3],[0,1,0,4,5],[0,0,0,0,0],[0,0,0,0,-5]] (the weights)

the expected output: It returns None if shortest path from source to all other nodes can be arbitrarily low (ideally tends to -inf) because of negative cycles.
Otherwise the array of shortest distances from source to all other nodes is returned.

the output observed:

Vertex Distance from Source (0)
0	-	0
1	-	3
2	-	2
3	-	1
4	-	6

hence the following problem has been solved!
