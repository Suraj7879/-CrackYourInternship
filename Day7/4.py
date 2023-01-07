# https://leetcode.com/problems/majority-element/description/
# Time: O(n), Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

            if hashMap[nums[i]] > int(len(nums)/2):
                return nums[i]

