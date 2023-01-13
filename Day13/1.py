# https://leetcode.com/problems/power-of-two/submissions/877551528/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)