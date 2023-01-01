#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # st = set(nums)
        # for id, num in enumerate(st):
        #     nums[id] = num
        # return len(st)
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx+=1
        return idx
