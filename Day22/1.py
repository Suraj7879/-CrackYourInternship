# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = [[False for i in range(COLS)] for i in range(ROWS)]
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and visited[i][j] == False:
                    dfs(i, j, grid, visited)
                    count += 1
        return count
    
def dfs(i, j, grid, visited):
    rows, cols = len(grid), len(grid[0])
    if(min(i, j) < 0 or i == rows or j == cols or visited[i][j] == True or grid[i][j] == "0"):
        return 
    
    visited[i][j] = True
    dfs(i+1, j, grid, visited)
    dfs(i, j+1, grid, visited)
    dfs(i-1, j, grid, visited)
    dfs(i, j-1, grid, visited)




    
    
    