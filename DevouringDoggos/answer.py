class Item:
    def __init__(self, name, weight, value):
        self.name: str = name
        self.weight: int = weight
        self.value: int = value


def get_capacity(lines: str) -> int:
    return int(lines.splitlines()[1])


def get_total_items(lines: str) -> int:
    return int(lines.splitlines()[0])


def dog_devour(lines: str) -> list[str]:
    total_items = get_total_items(lines)
    total_capacity = get_capacity(lines) + 1

    possessionWeights = [[0 for _ in range(total_capacity)] for _ in range(total_items)]
    items = []

    linestr = str(lines).splitlines()[2:]
    for line in linestr:
        dogItem = line.split(' ')
        items.append(Item(" ".join(dogItem[:-2]), int(dogItem[-2]), int(dogItem[-1])))

    def calculate_devour():
        for current_item in range(0, total_items):

            for cur_weight in range(0, total_capacity):

                # Initialize class items
                item = items[current_item]

                # print(item.name, item.weight, item.value)

                # Do Calculations, subtract the current weight
                # in the matrix by the current item weight.
                calc_weight = cur_weight - item.weight
                if calc_weight < 0 or item.weight > total_capacity:
                    possessionWeights[current_item][cur_weight] = max(possessionWeights[current_item][cur_weight], possessionWeights[current_item - 1][cur_weight])
                else:
                    possessionWeights[current_item][cur_weight] = \
                        max(item.value + possessionWeights[current_item - 1][calc_weight],
                            possessionWeights[current_item][cur_weight], possessionWeights[current_item - 1][cur_weight])
            # print(possessionWeights)
    calculate_devour()

    dogChoices = []
    start_row = total_items - 1
    start_col = total_capacity - 1

    # Lookup all possible Choices
    for i in range(total_items):
        if start_row > 0:
            if possessionWeights[start_row - 1][start_col] == possessionWeights[start_row][start_col]:
                start_row -= 1
                continue
        if possessionWeights[start_row][start_col] == 0:
            break
        dogChoices.insert(0, items[start_row].name)
        start_col -= items[start_row].weight
        start_row -= 1

    for choice in dogChoices:
        print(choice)
    print(possessionWeights[-1][-1])


if __name__ == "__main__":
    # Get the filename from stdin
    filename: str = input()

    # Read said file
    with open(filename, 'r') as file:
        file_contents = file.read()

    # Actually do the work
    dog_devour(file_contents)
