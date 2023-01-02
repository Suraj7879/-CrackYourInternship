# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

#Time: O(n), Space: O(N)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lst = []
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
            if hashMap[num] == 2:
                lst.append(num)
        return lst