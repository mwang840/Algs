"""Use a brute force algorithm to solve the
   "Nearest Neighbor Problem". The algorithm takes in a sequence of distances in a 2d adj matrix and follows the nearest neighbor algorithm
   """
import heapq


def to_matrix(lines: str) -> int:
    count = 0
    matrix = (lines.split("\n"))
    for line in range(len(matrix)):
        matrix[line] = matrix[line].split(' ')
        for li in range(len(matrix)):
            matrix[line][li] = int(matrix[line][li])
            count = count + 1
    print(matrix)
    return matrix


def get_ada_location_bf(location: list[list[int]]) -> list[int]:
    visited = [False]
    list_of_ada_path = []
    ada_distance_total = 0
    min_val = 0
    for loc in location:
        for l in loc:
            if min_val not in visited:
                visited.append(min_val)
                min_val = (heapq.nsmallest(2, l))[-1]
                list_of_ada_path.append(min_val)
                min_val = loc.index(min_val)

    print(list_of_ada_path)

    return list_of_ada_path, ada_distance_total


"""
Helper function to find the minmum distance between some vertex and the other unvisited vertex
"""
def findMinAdaDistance(initial_ada_distance: int, list_of_ada_distances, distances):
    min_distance = 42069
    min_neigbhor = 0
    for ada_neighbor in range(list_of_ada_distances):
        current_distance = distances[initial_ada_distance][ada_neighbor]
        if current_distance < min_distance:
            min_distance = current_distance
            min_neigbhor = ada_neighbor
    return min_neigbhor


if __name__ in "__main__":
    (get_ada_location_bf(to_matrix("0 3 4 2 7\n3 0 4 6 3\n4 4 0 5 8\n2 6 5 0 6\n7 3 8 6 0")))
