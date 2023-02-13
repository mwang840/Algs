'''
This function takes in a list of strings and finds the sum of those strings (int).
This function ignores the negative ints and exits once the input is -999
'''
def summation(sequence: list[int])->int:
    sum = 0
    """In this case I'm going to use pythons all function which will check if ALL elements of the array are negative OR the list is empty"""
    if all((seq < 0 for seq in sequence) or len(sequence) == 0):
           return "EMPTY"
    for seq in (sequence):
        """Checks to see if the value of the sequence AT that position is greater than -1, this should IGNORE all negatives"""
        if seq >= 0:
            sum = sum + seq
        """Have a case where the value is -999 we stop and return the sum"""
        if seq == -999:
            return sum
        """Another check where ALL the values are negative, thus we print out empty"""
    return sum
        

def main():
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    # Actually do the work
    #first apply list comprehension that I found (https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int)
    intlines = [int(x) for x in lines]
    summation(intlines)


if __name__ == "__main__":
    # Get the filename from stdin
    main()