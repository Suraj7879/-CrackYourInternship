# https://leetcode.com/problems/container-with-most-water/

#1. Bruteforce Solution (TLE)
# Time: O(N^2), Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW = 0
        for i in range(len(height)):
            for j in range(len(height)):
                ht = min(height[i], height[j])
                maxW = max(maxW, ht * (j-i))
        return maxW

#2. Using 2 pointer Approach
# Time: O(N), Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW = 0
        left = 0
        right = len(height)-1
        while left < right:
            ht = min(height[left], height[right])
            maxW = max(maxW, ht * (right-left))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxW