"""
Created by: Daniel Biocchi
Course Code: COSC4427   A21SP
Due Date: 5/22/2021

The N-queens puzzle is the problem of placing N queens on an N × N chessboard such that no two queens
attack each other.
Given an integer N (1 ≤ N ≤ 10), return all distinct solutions to the N-queens puzzle. The table below
shows the number of solutions and the number of unique solutions (without any rotations and reflections).
"""
class QueensPuzzle():

    # Class Variables
    upDiag = []
    downDiag = []
    colArray = []
    board = 0
    # Board size N x N
    N = 0
    solutions = 0
    allSolutionsArr = ()

    def __init__(self, N):
        """
        Constructor
        :param N: board size(N x N)
        """
        print("A new shape has been created!")
        self.N = N
        self.colArray = [0] * N
        self.upDiag = [0] * N * N
        self.downDiag = [0] * N * N
        self.board = [[0 for c in range(N)] for r in range(N)]
        self.displayBoard()
        self.findASafePlace(0)

    def findASafePlace(self, col):
        """
        Recursive function to find a safe place for the queen. Placing all queens or exiting
        :param col: what column to work on
        :return: boolean
        """
        # If a solution is found
        if col >= self.N:
            self.solutions = self.solutions + 1
            print(" ======= Solution : ", self.solutions, "=======")
            self.displayBoard()

        # If a solution is yet to be found
        for i in range(self.N):
            if self.isSafe(i, col):
                self.placeQueen(i, col)
                # Recursive call
                if bool(self.findASafePlace(col + 1)):
                    # True
                    return 1
                # Queen is not safe
                # Therefore, we backtrace
                self.removeQueen(i, col)
        return 0

    def isSafe(self, r, c):
        """
        Checks to see if the queen can be placed at passed location (r, c)
        :param r: row
        :param c: column
        :return: boolean
        """
        return not any([self.colArray[r], self.upDiag[r+c], self.downDiag[r - c + self.N - 1]])

    def removeQueen(self, r, c):
        """
        Remove the queen at location on the board (r, c)
        :param r: row
        :param c: column
        :return: void
        """
        self.board[r][c] = 0
        self.colArray[r] = 0
        self.upDiag[r+c] = 0
        self.downDiag[r-c+self.N-1] = 0

    def placeQueen(self, r, c):
        """
        Places a queen on the board and updates the relevant class data members.
        :param r: row
        :param c: column
        :return: void
        """
        self.upDiag[r + c] = 1
        self.board[r][c] = 1
        self.colArray[r] = 1
        self.downDiag[r-c+self.N-1] = 1
        next

    def displayBoard(self):
        """
        Display the 2D array (board) in 2 dimensions to stdout
        :return: void
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()
