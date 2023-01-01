#https://leetcode.com/problems/find-the-duplicate-number/description/
#BruteForce Way

#Time: O(NlogN), Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]

# using array to count the occurrence
#Time: O(N), Space: O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = [0 for i in range(len(nums))]
        for i in nums:
            temp[i] += 1
            if temp[i] > 1:
                return i