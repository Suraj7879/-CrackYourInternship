# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        backtrack(0, s, [], res)
        return res

def backtrack(idx, n, subS, res):
    if idx == len(n):
        res.append(subS)
        return
    for i in range(idx+1, len(n)):
        if isPalindromic(idx, i, n):
            print(idx, end="")
            print(i)
            backtrack(idx+i, n, subS + [n[idx:i]], res)

def isPalindromic(idx, i, n):
    while idx <= i:
        if n[idx] != n[i]:
            return False
        idx += 1
        i -= 1
    return True

