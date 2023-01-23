# https://leetcode.com/problems/flood-fill/description/

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         m, n = len(image), len(image[0])
#         initialColor = image[sr][sc]
#         visited = [[False for i in range(m)] for i in range(n)]
#         dfs(m, n, sr, sc, image, initialColor, color)
#         return image

# def dfs(m, n, sr, sc, image, initialColor, color):
#     if(min(sr, sc) < 0 or sr == m or sc == n or image[sr][sc] != initialColor):
#         return 
    
#     image[sr][sc] = color
#     dfs(m, n, sr+1, sc, image, initialColor, color)
#     dfs(m, n, sr-1, sc, image, initialColor, color)
#     dfs(m, n, sr, sc+1, image, initialColor, color)
#     dfs(m, n, sr, sc-1, image, initialColor, color)

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         m, n = len(image), len(image[0])
#         visited = [[False for i in range(n)] for i in range(m)]  # fix the dimensions of visited
#         dfs(m, n, sr, sc, image, visited, color)
#         return image

# def dfs(m, n, sr, sc, image, visited, color):
#     if sr < 0 or sr >= m or sc < 0 or sc >= n or visited[sr][sc]:
#         return
    
#     image[sr][sc] = color
#     visited[sr][sc] = True
    
#     dfs(m, n, sr+1, sc, image, visited, color)
#     dfs(m, n, sr-1, sc, image, visited, color)
#     dfs(m, n, sr, sc+1, image, visited, color)
#     dfs(m, n, sr, sc-1, image, visited, color)



class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visited = [[False for i in range(n)] for i in range(m)]
        initial = image[sr][sc]
        dfs(m, n, sr, sc, image, visited, color, initial)
        return image

def dfs(m, n, sr, sc, image, visited, color, initial):
    if(min(sr, sc) < 0 or sr == m or sc == n or visited[sr][sc] == True or image[sr][sc] != initial):
        return 

    if image[sr][sc] == color:
        return image

    image[sr][sc] = color
    visited[sr][sc] == True
    dfs(m, n, sr+1, sc, image, visited, color, initial)
    dfs(m, n, sr-1, sc, image, visited, color, initial)
    dfs(m, n, sr, sc+1, image, visited, color, initial)
    dfs(m, n, sr, sc-1, image, visited, color, initial)














# from queue import Queue
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         m = len(image)
#         n = len(image[0])
#         tempColor = image[sr][sc]
#         bfs(m, n, image, sr, sc, color, tempColor)
#         return image


# def bfs(m, n, image, sr, sc, color, tempColor):
#     visited = [[False for i in range(n)] for i in range(m)]
#     print(visited)
#     q = Queue()
#     q.put((sr, sc))
#     while not q.empty():
#         sr, sc = q.get()
#         visited[sr][sc] = True
#         image[sr][sc] = color
        
#         for dsr, dsc in [(sr + 1, sc), (sr - 1, sc), (sr, sc+1), (sr, sc-1)]:
#             if 0 <= dsr < m and 0 <= dsc < n and visited[dsr][dsc] == False and image[dsr][dsc] == tempColor:
#                 q.put((dsr, dsc))





# def dfs(m, n, image, sr, sc, color, tempColor):
#     if color == tempColor:
#         return 
#     if image[sr][sc] == tempColor:
#         image[sr][sc] = color
#         if sr >= 1:
#             dfs(m, n, image, sr-1, sc, color, tempColor)
#         if sc >= 1:
#             dfs(m, n, image, sr, sc-1, color, tempColor)
#         if sr+1 < m:
#             dfs(m, n, image, sr+1, sc, color, tempColor)
#         if sc+1 < n:
#             dfs(m, n, image, sr, sc+1, color, tempColor)


    


    # image[sr][sc]
    # bfs(image, sr+1, sc, color)
    # bfs(image, sr, sc+1, color)
    # bfs(image, sr-1, sc, color)
    # bfs(image, sr, sc-1, color)
