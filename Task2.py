#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
#
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 5, part 2
    Read a text file named "book.txt" that may have multiple lines.  Then create 
a "summary.txt" file that has the frequency of each letter, case-insensitive, 
i.e., the "a" and "A" are the same letter.  Each line has a record of the letter
and frequency.  The last line should be a summary to tell if the file has all 
26 letters.  A sample "summary.txt" is:
A 25
C 36
...
Y 2
Z 4
It doesn't have all letters.
    Another "book.txt" may generate the "summary.txt" as the following:
A 25
B 36
...
X 2
Y 1
Z 4
It has all letters.

"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables
BookText = ''   # Record of the book file's text
Alphabet  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
AlphaList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#########1#########2#########3#########4#########5#########6#########7#########8
# Function(s)
#--------1---------2---------3---------4---------5---------6---------7---------8#

#--------1---------2---------3---------4---------5---------6---------7---------8#
#########1#########2#########3#########4#########5#########6#########7#########8
# Main
#  Read the book.txt file
try:
    with open('book.txt',mode='r') as BookText:     # Open the text file book.txt
        for BookLine in BookText:                   # Reading line by line of text
            for EachChar in BookLine:               # Reading char by char of line
                ASCIIChar = ord(EachChar)           # Convert char to ASCII value
                if (ASCIIChar == 13):               # Check for newline or Carriage Return
                    break                           # If CR detected, break out; new line
                elif ((ASCIIChar >= 65) and         # If char in UPPERCASE set
                      (ASCIIChar <= 90)):           # then
                      AlphaList[ASCIIChar-65] += 1  # increment count of AlphaList
                elif ((ASCIIChar >= 97) and         # If char in lowercase set
                      (ASCIIChar <= 122)):          # then
                      AlphaList[ASCIIChar-97] += 1  # increment count of AlphaList
except:
    print('The file \'book.txt\' does not exist.')
    quit()

OutString = "It has all letters."               # Set default OutString value
for i in range(0,26):                           # Check counts in AlphaList
    if AlphaList[i] == 0:                       # If value == 0
        OutString = "It doesn\'t have all letters." # then set OutString to alternate statement
        break                                   # stop checking for 0 value

with open('summary.txt', mode='w') as BookText: # Open output file to write
    for i in range(0,26):                       # Retrieve each list value & 
        print(f'{Alphabet[i]} {AlphaList[i]}',file=BookText)    # print label & value to file
    print(f'{OutString}',file=BookText)         # Print summary
    
# End Main
#########1#########2#########3#########4#########5#########6#########7#########8