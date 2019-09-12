from board import Board
import numpy as np



class Genetic:
    boards = []

    def __init__(self, n):
        self.step = 0
        for i in range(4):
            self.boards.append(Board(n))
            self.boards[i].set_queens()

    def readBoard(self, board):
        string = []
        for i in range(len(board.map)):
            for j in range(len(board.map[i])):
                if (board.map[i][j] == 1):
                    string.append(j)
        return string

    def chooseParents(self):
        fit = self.findFitnesses()
        low_fit = np.argmin(fit)
        fit.pop(low_fit)
        self.boards.pop(low_fit)

    def findFitnesses(self):
        fit = []
        for i in range(len(self.boards)):
            self.boards[i].fitness()
        for i in range(len(self.boards)):
            self.boards[i].show()
        for i in range(len(self.boards)):
            fit.append(self.boards[i].fit)
        return fit
            


if __name__ == '__main__':
    test = Genetic(5)
    test.chooseParents()
    for i in range(len(test.boards)):
        test.boards[i].show()