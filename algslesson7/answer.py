'''
A student log consists of three numbers and a letter, separated by spaces (in the form "Number, Letter, Number, Number"). All numbers will be 32-bit integers (i.e., no more than 2^31).

The first element is the Student ID , a unique number representing that student inside the dataset.
The second element is the Action Code , and will be either the letter "P", "S", or "T"
If the letter is "P", for "Page Open", then the third element will be the Page ID (a number) of the page opened by the student.
If the letter is "S", for "Submission Scored", then the third element will be the score of the Submission made by the student (a number).
If the letter is "T", for "Temperature Tracked", then the third element will be the current Temperature of the student (a number in Fahrenheit).
The fourth element is the Timestamp , a number representing when the record was made.
An example of several records are below:

507 P 1000 1
1 S 6 2
1 P 1400 3
1 S 8 8
1 T 101 10
507 S 4 12
1 P 1700 15
1 S 7 16
507 S 8 20
'''
from operator import attrgetter

class Student:
    ##A constructor that takes in the studentId, the current page number (if the code is P) and the current number of assignments graded (if the code is S)
    def __init__(self, studentId: int, latestPageNum: int, numOfAssignmentsScore: int):
        self.studentId = studentId
        self.lowestPageNum = -1
        self.latestPageNum = latestPageNum
        self.numOfAssignmentsScore = numOfAssignmentsScore
        self.submissionCount = 0
        
    ##repr model, prints out the object
    def __repr__(self):
        return f'{self.studentId} {self.latestPageNum} {self.numOfAssignmentsScore}'
    ##Method to handle submission scores if the Action Code is an 'S'



def sort_log_data(log: list[str]):
    students_to_handle = {}
    totalLines = int(log[0].strip())
    for lines in range(1, totalLines + 1):
        '''
        Split the log file to four elements in the string respectfully
        '''
        studentId, actionCode, value, timeSpent = log[lines].strip()
        value = int(value)
        timeSpent = int(timeSpent)
        '''
        If the student is not in the dictionary, place it in and check if the student opens a page or submits an assignment
        '''
        if studentId not in students_to_handle and (actionCode == "P" or actionCode == "S"):
            students_to_handle[studentId] = Student(studentId)

        '''Checks if the actionCode is P'''
        if actionCode == "P":
            if students_to_handle[studentId].lowestPageNum == -1 or students_to_handle[studentId].lowestPageNum > value:
                students_to_handle[studentId].lowestPageNum = value
                ##Students latest page number is being updates
                students_to_handle[studentId].latestPageNum = value
        elif actionCode == "S":
            students_to_handle[studentId].submissionCount += 1
            students_to_handle[studentId].numOfAssignmentsScore += value
        elif actionCode == "T":
            pass    
    averageScore = students_to_handle[studentId].numOfAssignmentsScore / students_to_handle[studentId].submissionCount
    '''
    Convert dictionary to list and then call sort to sort it in order.
    '''
    sortedList = sorted(students_to_handle, key=attrgetter("lowestPageNum", "latestPageNum", "averageScore"))
    for sort in sortedList:
        if sort.lowestPageNum >= 0 and sort.submissionCount >= 1:
            print(sort)
    return sortedList


def main():
    list = ["507 P 1000 1 1 S 6 2 1 P 1400 3 1 S 8 8 1 T 101 10 507 S 4 12 1 P 1700 15 1 S 7 16 507 S 8 20"]
    (sort_log_data(list))

if __name__ in "__main__":
    main()    