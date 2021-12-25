# This module contains three functions
# These functions do not require any information about an instance or class
# and are thus not written as part of a class

def printInstructions(instruction):
    print(instruction)


def getUserScore(userName):
    """This function accepts the user name as a parameter, opens a file
       containing user scores, reads the file using a for loop, and returns
       closes the file, and returns the user's score beside the username.
       The function is nested within a try/except block to handle an IOError
       if one occurs."""
    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(', ')
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return '-1'


def updateUserScore(newUser, userName, score):
    """" This function relies on the remove and rename functions from the os module
           to remove the file and rename the file to UserScores.txt.
           If newUser is True, UserScores.txt is opened in append mode and the user's
           username and score are written to UserScores.txt using the write function.
           If newUser is False, the user's username and score are written to the file,
           we create a temporary file for this purpose"""
    from os import remove, rename

    if newUser == True:
        input = open('userScores.txt', 'a')
        input.write(userName + ', ' + score + '\n')
        input.close()
    else:
        temp = open('userScores.tmp', 'w')
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(', ')
            if content[0] == userName:
                temp.write(userName + ', ' + score + '\n')
            else:
                temp.write(line)

        input.close()
        temp.close()

        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
