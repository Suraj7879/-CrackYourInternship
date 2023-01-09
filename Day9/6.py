# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Using input output method --> Aditya Verma
        lst = []
        openn = n
        close = n
        op = "" 
        recur(openn, close, op, lst)
        return lst

def recur(openn, close, op, lst):
    if openn == 0 and close == 0:
        lst.append(op)
        return
    if(openn != 0):
        op1 = op
        op1 += "("
        recur(openn-1, close, op1, lst)
    
    if(close > openn):
        op2 = op
        op2 += ")"
        recur(openn, close-1, op2, lst)
    
    return 