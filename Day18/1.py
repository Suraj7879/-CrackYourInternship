# https://leetcode.com/problems/permutations-ii/description/

# using extra space
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = [False for i in range(len(nums))]
        backtrack(nums, [], res, 0, visited)
        return res

def backtrack(nums, temp, res, idx, visited):
    if idx == len(nums) and temp not in res:
        res.append(temp)
        return res
    
    for i in range(len(nums)):
        if visited[i] is False:
            visited[i] = True
            backtrack(nums, temp + [nums[i]], res, idx+1, visited)
            visited[i] = False

# by using swapping technique

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        backtrack(nums, res, 0)
        return res

def backtrack(nums, res, idx):
    if idx == len(nums) and nums not in res:
        res.append(nums[:])
        return res
    
    for i in range(idx, len(nums)):
        nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(nums, res, idx+1)
        nums[idx], nums[i] = nums[i], nums[idx]

# def backtrack(nums, res, idx):
#     if idx == len(nums) and nums not in res:
#         res.append(nums)
#         return res
    
#     for i in range(idx, len(nums)):
#         nums[idx], nums[i] = nums[i], nums[idx]
#         backtrack(nums, res, idx+1)
#         nums[idx], nums[i] = nums[i], nums[idx]