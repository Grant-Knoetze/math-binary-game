# This module contains three functions
# These functions do not require any information about an instance or class
# and are thus not written as part of a class

from os import remove, rename


def printInstructions(instruction):
    return str(instruction)


try:
    def getUserScore(userName):
        with open("UserScores.txt", "r") as file:
            for line in userName:
                line.split()
                if userName == userName:
                    return line
                    file.close()
                else:
                    return "-1"
                file.close()
                print(line)

except IOError:
    print("File not found")
    open("UserScores.txt", "w")
    print("-1")
    "UserScores.txt".close()




