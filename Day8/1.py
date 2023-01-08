# https://leetcode.com/problems/game-of-life/description/
# Approach: 1
# Time: O(8*n*m), Space: O(n*m)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #apply by using:
        #    under-population: < 2 ---> 0
        #    live to next generation: 2 or 3 ---> 
        #    over-population: > 3
        #    reproduction: == 3

        clone = [[None for i in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                clone[i][j] = board[i][j]

        directions = [[-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 0], [0, 1],[1, 1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neigh = 0
                for m in directions:
                    g1, g2 = m
                    np1, np2 = i+g1, j+g2
                    if 0 <= np1 < len(board) and 0 <= np2 < len(board[0]):
                        if clone[np1][np2] == 1:
                            neigh += 1
                
                if clone[i][j] == 1:
                    if neigh == 2 or neigh == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                
                elif clone[i][j] == 0 and neigh == 3:
                    board[i][j] = 1




