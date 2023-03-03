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
        studentId = 0
        lowestPageNum = 0
        latestPageNum = 0
        numOfAssignmentsScore = 0
        submissionCount = 0
        averageScore = 0
    
    ##Method to handle submission scores if the Action Code is an 'S'



def sort_log_data(log: list[str]):
    students_to_handle = {}
    totalLines = log[0]
    log.pop(0)
    logList = []
    for r in range(int(totalLines)):
        logList.append(log[r].split())
    
    
    for lines in range(len(logList)):
        '''
        Split the log file to four elements in the string respectfully
        '''
        '''
        If the student is not in the dictionary, place it in and check if the student opens a page or submits an assignment
        '''
        if students_to_handle.get(logList[lines][0]):
            currentStudent = students_to_handle.get(logList[lines][0])
            if logList[lines][1] == "P":
                currentStudent.latestPageNum = int(logList[lines][2])
                if int(currentStudent.lowestPageNum) > int(logList[lines][2]) or int(currentStudent.lowestPageNum) == 0:
                    currentStudent.lowestPageNum = int(logList[lines][2])
            elif logList[lines][1] == "S":
                currentStudent.numOfAssignmentsScore += int(logList[lines][2])
                currentStudent.submissionCount += 1
                currentStudent.averageScore = int(int(currentStudent.numOfAssignmentsScore)/int(currentStudent.submissionCount)) 
            
        else:
            aNewStudent = Student()
            aNewStudent.studentId = logList[lines][0]
            if logList[lines][1] == "P":
                aNewStudent.lowestPageNum = int(logList[lines][2])
                aNewStudent.latestPageNum = int(logList[lines][2])

            elif logList[lines][1] == "S":
                aNewStudent.submissionCount += 1
                aNewStudent.numOfAssignmentsScore += int(logList[lines][2])
            students_to_handle[logList[lines][0]] = aNewStudent     

        ##averageScore = students_to_handle[studentId].numOfAssignmentsScore / students_to_handle[studentId].submissionCount
    '''
    Convert dictionary to list and then call sort to sort it in order.
    '''
    studentList = []
    for studentName in students_to_handle.values():
        studentList.append(studentName)

    studentString = ""
    sortedList = sorted(studentList, key=attrgetter("lowestPageNum", "latestPageNum", "averageScore"))
    for sort in studentList:
        if int(sort.latestPageNum) != 0 and int(sort.averageScore) != 0:
            studentString += str(sort.studentId) + " " + str(sort.lowestPageNum) + " " +  str(sort.latestPageNum) + " " + str(sort.averageScore) + "\n" 
            print(sort.studentId, sort.lowestPageNum, sort.latestPageNum, sort.averageScore)
    return sortedList



if __name__ == "__main__":
    
    # Get the filename from stdin
    
    
    
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    # Actually do the work
    sort_log_data(lines)
    