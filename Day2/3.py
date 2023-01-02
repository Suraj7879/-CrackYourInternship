# https://leetcode.com/problems/two-sum/description/
#Time: O(n), Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSum = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in hashSum:
                return [i, hashSum[toFind]]
            hashSum[nums[i]] = i