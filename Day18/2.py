# https://leetcode.com/problems/word-search-ii/description/

# Getting TLE with this brute force solution, should be done using Trie (Have to study)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]
        for i in words:
            word = i
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == word[0]:
                        backtrack(r, c, word, board, "", res, visited, 0)
        
        return res

def backtrack(r, c, word, board, temp, res, visited, idx):

    if min(r, c) < 0 or visited[r][c] == True or idx == len(word) or board[r][c] != word[idx]:
        return

    if len(temp) == len(word):
        res.append(word)
        return
    
    visited[r][c] =
    backtrack(r+1, c, word, board, temp + board[r][c], res, visited, idx+1)
    backtrack(r, c+1, word, board, temp + board[r][c], res, visited, idx+1)
    backtrack(r-1, c, word, board, temp + board[r][c], res, visited, idx+1)
    backtrack(r, c-1, word, board, temp + board[r][c], res, visited, idx+1)


