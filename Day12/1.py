# https://leetcode.com/problems/missing-number/submissions/876895326/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n = n ^ i
        
        for i in range(len(nums)+1):
            n = n ^ i
        
        return n