from board import Board
import numpy as np
import copy as cp
import random

class queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class queens:
    Queens = []
    board = Board(0)
    depth = 0
    count = 0
    def __init__(self, board):
        self.board = board
        for row in range(len(board.map)):
            for column in range(len(board.map[0])):
                if (board.map[row][column] == 1):
                    self.Queens.append(queen(row, column))

    def solveQueen(self):
        
        print(self.totalConflicts())
        while(self.totalConflicts() != 0):
            for i in range(len(self.Queens)):
                if (self.findConflicts(i) != 0):
                    self.randomMove(i)
        print("The number of required steps:", self.count)
        return self.board

    def potentialMoves(self, q):
        moveList = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = q.x + i
                y = q.y + j
                if ( x >= 0 and y >= 0 and x < len(self.board.map[0]) and y < len(self.board.map[0])):
                    if(self.board.map[x][y] == 0):
                        moveList.append(queen(x, y))
        return moveList

    def randomMove(self, queenNum):
        moves = []
        snapshot = cp.deepcopy(self.Queens[queenNum])
        self.count = self.count + 1
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = self.Queens[queenNum].x + i
                y = self.Queens[queenNum].y + j
                if ( x >= 0 and y >= 0 and x < len(self.board.map[0]) and y < len(self.board.map[0])):
                    if(self.board.map[x][y] == 0):
                        moves.append(queen(x, y))
        randomMove = random.randint(0, len(moves)-1)
        self.board.map[snapshot.x][snapshot.y] = 0
        self.Queens[queenNum] = moves[randomMove]
        self.board.map[moves[randomMove].x][moves[randomMove].y] = 1
        self.depth = self.depth + 1
        if (self.findConflicts(queenNum) == 0):
            return 0
        elif (self.depth < 5):
            self.randomMove(queenNum)
        else:
            self.depth = 0
            return -1

    def totalConflicts(self):
        number = 0
        for i in range(len(self.Queens)):
            number = number + self.findConflicts(i)
        return number

    def findConflicts(self, queenNum):
        conflict = 0
        count = 0
        #row conflict
        for row in range(len(self.board.map[0])):
            if(self.board.map[self.Queens[queenNum].x][row] == 1):
                count = count + 1
        conflict = conflict + count - 1
        count = 0
        #column conflict
        for column in range(len(self.board.map[0])):
            if(self.board.map[column][self.Queens[queenNum].y] == 1):
                count = count + 1
        conflict = conflict + count - 1
        count = 0
        #diag
        x, y = self.Queens[queenNum].x, self.Queens[queenNum].y
        while (x > 0 and y > 0):
            x = x - 1
            y = y - 1
            if (x >= 0 and y >= 0):
                if (self.board.map[x][y] == 1):
                    count = count + 1
        conflict = conflict + count
        count = 0
        #######################################################
        x, y = self.Queens[queenNum].x, self.Queens[queenNum].y
        while (x < len(self.Queens) and y < len(self.Queens)):
            x = x + 1
            y = y + 1
            if (x < len(self.Queens) and y < len(self.Queens)):
                if (self.board.map[x][y] == 1):
                    count = count + 1
        conflict = conflict + count
        count = 0
        #########################################################
        x, y = self.Queens[queenNum].x, self.Queens[queenNum].y
        while (x > 0 and y < len(self.Queens)):
            x = x - 1
            y = y + 1
            if (x >= 0 and y < len(self.Queens)):
                if (self.board.map[x][y] == 1):
                    count = count + 1
        conflict = conflict + count
        count = 0
        #########################################################
        x, y = self.Queens[queenNum].x, self.Queens[queenNum].y
        while (x < len(self.Queens) and y > 0):
            x = x + 1
            y = y - 1
            if (x < len(self.Queens) and y >= 0):
                if (self.board.map[x][y] == 1):
                    count = count + 1
        conflict = conflict + count
        count = 0
        return conflict

class Hill_Climb:
    def __init__(self, n):
        self.step = 0


if __name__ == '__main__':
    home = Board(5)
    home.set_queens()
    qn = queens(home)
    home = qn.solveQueen()
    home.fitness()
    home.show()