# https://leetcode.com/problems/set-matrix-zeroes/description/
# Bruteforce Approach
# Time: O(N^2), Space: O(N^2)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        duplicate = [[None for i in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                duplicate[i][j] = matrix[i][j]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if duplicate[row][col] == 0:
                    for i in range(len(matrix[0])):
                        matrix[row][i] = 0
                    for j in range(len(matrix)):
                        matrix[j][col] = 0     
# Optimal Approach
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        duplicate = [[None for i in range(len(matrix[0]))] for i in range(len(matrix))]
        x = []
        y = []
        # Finding x and y coordinates and storing them seapratly, becuase we have make the entire row and col containing zero to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.append(i)
                    y.append(j)
        
        # Make rows zero row -> 0
        for i in range(len(x)):
            idx = x[i] 
            for j in range(len(matrix[0])):
                matrix[idx][j] = 0
        
        # Make cols zero col -> 0
        for i in range(len(y)):
            idx = y[i]
            for j in range(len(matrix)):
                matrix[j][idx] = 0

                
