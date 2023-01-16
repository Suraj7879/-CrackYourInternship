# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = [i for i in range(1, n+1)]
        idx = 0
        op = []
        backtrack(idx, lst, [], op, k)
        return op

def backtrack(idx, lst, tempOp, op, k):
    if idx == len(lst):
        if len(tempOp) == k:
            op.append(tempOp)
        return
    
    backtrack(idx+1, lst, tempOp+[lst[idx]], op, k)
    backtrack(idx+1, lst, tempOp, op, k)