"""Use a brute force algorithm to solve the
   "Nearest Neighbor Problem". The algorithm takes in a sequence of distances in a 2d adj matrix and follows the nearest neighbor algorithm
   """
import heapq


def to_matrix(lines: list[str]) -> int:
    count = 0
    matrix = lines
    for line in range(len(matrix)):
        matrix[line] = matrix[line].split(' ')
        for li in range(len(matrix)):
            matrix[line][li] = int(matrix[line][li])
            count = count + 1
    return matrix


def get_ada_location_bf(distances: list[list[int]]) -> list[int]:
    unvisited_ada_locations = set(range(1, len(distances)))
    visited_ada_locations = [0]
    ada_visit_place = 0
    totalCost = 0
    while len(unvisited_ada_locations) != 0:

        """
        Meme large distance number cuz why not
        """
        min_ada_distance = 42069
        for unvisited in unvisited_ada_locations:
            if ada_visit_place != unvisited:
                ada_min = distances[ada_visit_place][unvisited]
                if ada_min < min_ada_distance:
                    min_ada_distance = ada_min
                    ada_visit_place = unvisited
        unvisited_ada_locations.remove(ada_visit_place)
        visited_ada_locations.append(ada_visit_place)
    visited_ada_locations.append(visited_ada_locations[0])

    for ada_place, visited in enumerate(visited_ada_locations[0:-1]):
        if ada_place < len(visited_ada_locations):
            totalCost += distances[visited][visited_ada_locations[ada_place + 1]]

        elif ada_place > len(visited_ada_locations) - 1:
            totalCost += 0
    approximate_output = ""
    for index in range(len(visited_ada_locations) - 1):
        approximate_output = approximate_output + str(visited_ada_locations[index]) + "\n"
    approximate_output = approximate_output + str(totalCost)
    return approximate_output


if __name__ in "__main__":
    filename = input()
    with open(filename) as f: lines = f.readlines()
    ada_locations = to_matrix(lines)
    print(get_ada_location_bf(ada_locations))

