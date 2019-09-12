from board import Board
import numpy as np
import copy as cp
import random as rand


class Genetic:
    boards = []
    fit = []
    step = 0
    def __init__(self, n):
        for i in range(4):
            self.boards.append(Board(n))
            self.boards[i].set_queens()
        self.fit = self.findFitnesses()

    def solve(self):
        self.step = self.step + 1
        self.selection()
        self.crossover()
        self.fit = self.findFitnesses()
        if (10 in self.fit):
            print("The number of steps is:", self.step)
            high_fit = np.argmax(self.fit)
            self.boards[high_fit].show()
        else:
            self.solve()



    def crossover(self):
        strings = []
        for i in range(len(self.boards)):
            strings.append(self.readBoard(self.boards[i]))
        cpyStrings = [[],[],[],[]]
        randInt0, randInt1 = rand.randint(0, 4), rand.randrange(4, 5)
        for i in range(randInt0):
            cpyStrings[0].append(strings[0][i])
        for i in range(randInt0, 5):
            cpyStrings[0].append(strings[1][i])
        for i in range(randInt0):
            cpyStrings[1].append(strings[1][i])
        for i in range(randInt0, 5):
            cpyStrings[1].append(strings[0][i])

        for i in range(randInt1):
            cpyStrings[2].append(strings[2][i])
        for i in range(randInt1, 5):
            cpyStrings[2].append(strings[3][i])
        for i in range(randInt1):
            cpyStrings[3].append(strings[3][i])
        for i in range(randInt1, 5):
            cpyStrings[3].append(strings[2][i])

        self.mutation(cpyStrings)
        self.toBoard(cpyStrings)

    def toBoard(self, arr):
        for i in range(len(arr)):
            board = Board(5)
            for j in range(5):
                board.map[j][arr[i][j]] = 1
            self.boards[i] = board

    def mutation(self, arr):
        for i in range(len(arr)):
            arr[i][rand.randint(0, 4)] = rand.randint(0, 4)

    def readBoard(self, board):
        string = []
        for i in range(len(board.map)):
            for j in range(len(board.map[i])):
                if (board.map[i][j] == 1):
                    string.append(j)
        return string

    def selection(self):
        fit = self.findFitnesses()
        low_fit = np.argmin(fit)
        fit.pop(low_fit)
        high_fit = np.argmax(fit)
        self.boards.pop(low_fit)
        self.boards.append(self.boards[high_fit])

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