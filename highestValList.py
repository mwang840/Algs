def highestValList(values: list)->int:
    if len(values) == 0:
        return None
    highAf = values[0]
    i = 1
    for i in range(values):
        if values[i] > highAf:
            highAf = values[i]
        
    return highAf


def main():
    print(highestValList([5, 1, 2, 15, 29, 25, 26]))

if __name__ in "main":
    main()