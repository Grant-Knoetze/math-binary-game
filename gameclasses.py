# We will create three classes:
class Game:
    def __init__(self, noOfQuestions=0):
        self._noOfQuestions = noOfQuestions
        print("Creating game object")

    # Getter method to add a property returns the value of noOfQuestions:
    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("Minimum number of Questions = 1")
            print("Hence, number of questions will be set to 1.")
        elif value > 10:
            self._noOfQuestions = 10
            print("Maximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10.")
        else:
            self._noOfQuestions = value


# Binary game class:
class BinaryGame(Game):
    def __init__(self, noOfQuestions=0):
        super().__init__(noOfQuestions)
        print("Creating binary game object")

    def generateQuestions(self):
        from random import randint
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            input("Convert the number " + str(base10) + " to binary: ")
            userResult = input()
            while True:
                try:
                    answer = int(userResult, base = 2) # Convert the user input to base 2
                    if answer == base10:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print("Wrong answer. The correct answer is {:b}".format(base10))
                        break
                    open(userResult, "a")
                    userResult.append(userResult)
                    break
                except ValueError:
                    print("Please enter a valid number")
                    userResult = input()



