Currently, I have a solution, which I attempted to use the
nearest neighbor problem. I broke that problem
into a sub problems. I used a helper function to help 
find the minimum distance between vertices.
My algorithm takes in a list of strings with the distances,
each separated by a new line. I modeled my code off of the extreme algorithms site
specifically with the nearest neighbor (https://www2.seas.gwu.edu/~simhaweb/champalg/tsp/tsp.html).
I would say sitting down in office hours helped with this assignment as I was overthinking this assignment out.

Today I rewrote my helper function and just made
my output one function that took in a 2d martix and followed the
pseudocode. An greedy algorithm via nearest neighbor
is executed to find the shortest distances between nodes and finds the min distance.
Once we find the min distance, we add that vertex to the path
and once it is added to the path we return the path, and the lowest cost calculated from the path.
