# https://leetcode.com/problems/unique-paths-iii/description/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for i in range(col)] for i in range(row)]
        countt = 0
        sr = 0
        sc = 0
        ans = [0]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    sr = i
                    sc = j
                elif grid[i][j] == 0:
                    countt += 1
        
        backtrack(sr, sc, row, col, grid, countt, ans, visited)
        return ans[0]

def backtrack(sr, sc, row, col, grid, count, ans, visited):
    if(min(sr, sc) < 0 or sr == row or sc == col or grid[sr][sc] == -1 or visited[sr][sc] == True):
        return 

    if grid[sr][sc] == 2 and count == -1:
        ans[0] += 1
        return

    visited[sr][sc] = True
    backtrack(sr+1, sc, row, col, grid, count-1, ans, visited)
    backtrack(sr, sc+1, row, col, grid, count-1, ans, visited)
    backtrack(sr, sc-1, row, col, grid, count-1, ans, visited)
    backtrack(sr-1, sc, row, col, grid, count-1, ans, visited)
    visited[sr][sc] = False
    

        