#https://leetcode.com/problems/sort-colors/description/
#1. One direct way to solve this is using built in sort function, O(NlogN)
#2. Another would be to count the occurrences of each digit and then traverse in an array, which will run in O(2n), basically 2 for loops

#3. Optimsed solution using 3 ptr low, mid and high respectively(Also well known as Dutch national Flag anthem problem)
#Time: O(n), Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid]==0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
        return nums
