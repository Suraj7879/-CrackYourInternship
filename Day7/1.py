# https://leetcode.com/problems/word-search/description/

# Time: O(N * M * 4^K), Space: O(K), where K stands for word size

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board) 
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtrack(i, j, row, col, board, word, 0):
                        return True
        return False

def backtrack(i, j, m, n, board, word, k):
    #If k is equal to the given word's length, it means every character of word is present inside board[][], so we return true
    if len(word) == k:
        return True
    # If we are moving outside the board's boundary or if board[i][j] is not equal to word[k] , we return false
    if(min(i, j) < 0 or i==m or j==n or board[i][j] != word[k]):
        return
    # We store the Character present in the current Cell inside ch variable
    ch = board[i][j]
    # We change board[i][j] to "#"" so that we don't visit the Same Cell again
    board[i][j] = "#"
    op1 = backtrack(i+1, j, m, n, board, word, k+1)
    op2 = backtrack(i, j+1, m, n, board, word, k+1)
    op3 = backtrack(i-1, j, m, n, board, word, k+1)
    op4 = backtrack(i, j-1, m, n, board, word, k+1)
    # We backtrack and change the value of board[i][j] to it's original character stored in ch variable
    board[i][j] = ch

    #As we need to find the word, no matter from which direction we get it, so we return (op1 OR op2 OR op3 OR op4)
    return op1 or op2 or op3 or op4

