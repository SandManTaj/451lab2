from board import Board
import copy as cp
import random


class Hill_Climb:
    def __init__(self, n):
        self.step = 0
    
    def climb(b, n):
        for i in range(n):
            for j in range(n):
                if (b.map[i][j] == 1):
                    Hill_Climb.toAdjacent(b.map, i, j)



    def toAdjacent(b, i, j):
        validMove = False
        while (validMove == False):
            lr, ud = 0, 0
            while (lr == 0 and ud == 0):
                lr = random.randint(-1, 1)
                ud = random.randint(-1, 1)
            if (j + lr >= 0 and j + lr < len(b[0]) and i + ud >= 0 and i + ud < len(b)):
                if (b[i+ud][j+lr] == 0):
                    validMove = True
                    b[i][j] = 0
                    ud = i + ud
                    lr = j + lr
                    b[ud][lr] = 1
        return ud, lr


if __name__ == '__main__':
    n = 5
    home = Board(n)
    home.set_queens()
    home.show()
    Hill_Climb.climb(home, n)
    home.fitness()
    home.show()
