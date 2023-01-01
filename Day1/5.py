# https://leetcode.com/problems/move-zeroes/submissions/869123009/
# Time: O(N), Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums