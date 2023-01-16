# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idx = 0
        lst = nums
        n = len(lst)
        op = []
        backtrack(idx, lst, n, [], op)
        return op

def backtrack(idx, lst, n, opLst, op):
    if idx == n:
        if opLst not in op:
            op.append(opLst)
        return 
    
    backtrack(idx+1, lst, n, opLst + [lst[idx]], op)
    backtrack(idx+1, lst, n, opLst, op)

