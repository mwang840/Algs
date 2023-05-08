"""Use a brute force algorithm to solve the
   "Nearest Neighbor Problem". The algorithm takes in a sequence of distances in a 2d adj matrix
   """
def get_ada_location_bf(lines, distance):
    listOfDist = []
    vertex = lines
    for li in lines:
        small_dist = 10000000
        vertex_pt = 0
        for line in lines:
            if li[0] == line[0]:
                print("We have found a match")



