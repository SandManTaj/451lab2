#Tajbir Sandhu
#CECS 451
#9/12/2019

from board import Board
import numpy as np
import copy as cp
import random as rand


class Genetic:
    boards = []
    fit = []
    step = 0
    def __init__(self, n):
        #initializes 4 boards
        for i in range(4):
            self.boards.append(Board(n))
            self.boards[i].set_queens()
        #finds initial fitness
        self.fit = self.findFitnesses()

    #solves the boards recursively
    def solve(self):
        #increments the steps needed for the solution
        self.step = self.step + 1
        self.selection()
        self.crossover()
        self.fit = self.findFitnesses()
        #Shows the solution if found otherwise
        #solve calls itself
        if (10 in self.fit):
            print("The number of steps is:", self.step)
            high_fit = np.argmax(self.fit)
            self.boards[high_fit].show()
        else:
            self.solve()


    #finds the crossover from 4 parents
    def crossover(self):
        #stores the 4 parents as an array that is 
        #called string for some reason
        strings = []
        #populates strings[] with the locations of the queens
        for i in range(len(self.boards)):
            strings.append(self.readBoard(self.boards[i]))
        #stores the crossover results
        cpyStrings = [[],[],[],[]]
        #randomly selects 2 positions for the crossover to begin
        randInt0, randInt1 = rand.randint(0, 4), rand.randrange(4, 5)
        #crosses over the first and second string
        for i in range(randInt0):
            cpyStrings[0].append(strings[0][i])
        for i in range(randInt0, 5):
            cpyStrings[0].append(strings[1][i])
        for i in range(randInt0):
            cpyStrings[1].append(strings[1][i])
        for i in range(randInt0, 5):
            cpyStrings[1].append(strings[0][i])
        #crosses over the third and fourth string
        for i in range(randInt1):
            cpyStrings[2].append(strings[2][i])
        for i in range(randInt1, 5):
            cpyStrings[2].append(strings[3][i])
        for i in range(randInt1):
            cpyStrings[3].append(strings[3][i])
        for i in range(randInt1, 5):
            cpyStrings[3].append(strings[2][i])
        
        #mutates the strings
        self.mutation(cpyStrings)
        #updates the board with new queen positions
        self.toBoard(cpyStrings)

    #converts an array with positions to a board with queens
    def toBoard(self, arr):
        for i in range(len(arr)):
            board = Board(5)
            for j in range(5):
                board.map[j][arr[i][j]] = 1
            self.boards[i] = board

    #randomly mutates one gene in each string
    def mutation(self, arr):
        for i in range(len(arr)):
            arr[i][rand.randint(0, 4)] = rand.randint(0, 4)

    #converts queen positions into an array
    def readBoard(self, board):
        string = []
        for i in range(len(board.map)):
            for j in range(len(board.map[i])):
                if (board.map[i][j] == 1):
                    string.append(j)
        return string

    #removes the least fit potential parent
    def selection(self):
        fit = self.findFitnesses()
        low_fit = np.argmin(fit)
        fit.pop(low_fit)
        high_fit = np.argmax(fit)
        self.boards.pop(low_fit)
        self.boards.append(self.boards[high_fit])

    #finds the fitness for each parent
    def findFitnesses(self):
        fit = []
        for i in range(len(self.boards)):
            self.boards[i].fitness()
        for i in range(len(self.boards)):
            fit.append(self.boards[i].fit)
        return fit
            
if __name__ == '__main__':
    test = Genetic(5)
    test.solve()