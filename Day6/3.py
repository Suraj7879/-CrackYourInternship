# https://leetcode.com/problems/4sum/description/

# Time: O(n^3), Space: O(1)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if(i!=0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1, len(nums)-2):
                if(j!=i+1 and nums[j] == nums[j-1]):
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ == target:
                        temp = []
                        res.append((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif summ > target:
                        right -= 1
                    elif summ < target:
                        left += 1
        return set(res)

