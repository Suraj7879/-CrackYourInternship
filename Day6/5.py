# https://leetcode.com/problems/spiral-matrix/description/

#Time: O(N)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, down = 0, len(matrix) - 1
        lst = []
        while top <= down and left <= right:
            for i in range(left, right+1):
                lst.append(matrix[top][i])
            top+=1
            for i in range(top, down+1):
                lst.append(matrix[i][right])
            right-=1

            if(top <= down):
                for i in reversed(range(left, right+1)):
                    lst.append(matrix[down][i])
                down-=1
                
            if(left <= right):
                for i in reversed(range(top, down+1)):
                    lst.append(matrix[i][left])
                left+=1
        return lst

