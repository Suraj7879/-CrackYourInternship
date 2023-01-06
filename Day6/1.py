# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Time: O(n), Space: O(n)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        hashMap = {}
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ % k == 0:
                count+=1
            if summ-k in hashMap:
                count += hashMap[summ-k]
            if summ not in hashMap:
                hashMap[summ] = 0
            hashMap[summ] += 1
        return count


        

        

