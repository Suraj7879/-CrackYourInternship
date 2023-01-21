# https://leetcode.com/problems/climbing-stairs/description/

#Optimized DP Code

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
	        a, b = b, a + b
        return b