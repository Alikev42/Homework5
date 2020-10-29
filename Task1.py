#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
#
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 5, part 1
    Assume that a file containing a series of student scores is named "scores.txt".
It may have the following content:
Alice 69
Bob 89
Cindy 79
    Write a program that calculates the number of students and the average of all 
the scores stored in the file and print the output:
"The class average is 79 for 3 students."
    Also write the output to "log.txt" file.  You should use the with function.
    It should handle IOError exceptions that are raised when it fails to open the 
file, display an error message with the detail error exception and stop.  For 
example, it happens when there is no scores.txt in the current folder.
    For the following content, it should handle any ValueError exceptions that are 
raised when the items that are read from the score field are failed to be converted
to a number by printing an error message and skip the record.  There could be 
multiple error values to be ignored.  For example, the data could be:
Alice 69
Bob eighty-seven
Cindy 79
David 89
Eric abc
    For the above data, it should skip both Bob and Eric and display:
Bad score for Bob, ignored
Bad score value for Eric, ignored
The class average is 79 for 3 students.
    The log.txt file should have the same content as the above output.

"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules
import statistics

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables
ClassScores = []
ClassAvg = 0.0
ClassCount = 0
BadValues = 0

StrName = []
StuName = []
StrScore = []

#########1#########2#########3#########4#########5#########6#########7#########8
# Function(s)
#--------1---------2---------3---------4---------5---------6---------7---------8#
def Average(IntScores):
    # Local Variables
    ii = 0
    Denom = 0
    ScoreTotal = 0
    Result = 0

    # Average the score only if the score is non-negative
    for ii in range(len(IntScores)):
        if IntScores[ii] != -1:
            Denom += 1
            ScoreTotal += IntScores[ii]
    if Denom != 0:
        Result = ScoreTotal / Denom
    else:
        Result = 0
    
    # Returning the average of the values in the integer list
    return Result
#--------1---------2---------3---------4---------5---------6---------7---------8#
#########1#########2#########3#########4#########5#########6#########7#########8
# Main #
# Check for existence of data file, prevention of IO Error

#  Retrieve data from file
try: 
    with open('scores.txt',mode='r') as ScoreRecord:
        for Line in ScoreRecord:            # For each Line in the file,
            try:
                StrName, StrScore = Line.split()# read string name and string score
            except ValueError:
                StrName, StrScore = ('NoName', '-1')
            StuName.append(StrName)         # Append name to end of StuName list
            ClassScores.append(StrScore)    # Append StrScore to ClassScores list
            ClassCount += 1                 # Increment the count of students
        # Close file implicitly
except FileNotFoundError:                   # If the file doesn't exist, alert the user
    print('The file \'scores.txt\' does not exist.') # and 
    quit()                                  # exit the program without executing remaining code


# Check for non-numerical entries in ClassScores
for i in range(ClassCount):                 # Ranges 0 to ClassCount 
    if ClassScores[i].isnumeric():          # If the string can be read as numeric, then
        ClassScores[i] = int(ClassScores[i])# convert the value to an integer
    elif not(ClassScores[i].isnumeric()):   # If the string cannot be numeric, then
        ClassScores[i] = -1                 # change value of the score to -1
        BadValues += 1                      # Increment number of bad score entries

# Calculate the class average    
ClassAvg = Average(ClassScores)     # Call the Averaging function with ClassScores list

# Reset counter i
i = 0       

# Write output to the file
with open('log.txt',mode='w') as ScoreRecord:   # Open log.txt file
    for i in range(len(ClassScores)):           # If the score is -1, print error message
        if ClassScores[i] == -1:                # to the file and to the screen
            print(f'Bad score for {StuName[i]}, ignored.',file=ScoreRecord)
            print(f'Bad score for {StuName[i]}, ignored.')
    print(f'The class average is {ClassAvg:.2f} for {ClassCount-BadValues} students.',
          file=ScoreRecord)         # Print the average of the remaining scores to the file
    print(f'The class average is {ClassAvg:.2f} for {ClassCount-BadValues} students.')
                                    # Print the average of the remaining scores to the screen
  # Close file implicitly    
# End Main
#########1#########2#########3#########4#########5#########6#########7#########8