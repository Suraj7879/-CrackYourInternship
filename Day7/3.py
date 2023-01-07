# https://leetcode.com/problems/merge-sorted-array/description/
# Time: O(m+n), Space: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m-1
        temp = len(nums1)-1
        ptr2 = n-1
        
        while ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2] and ptr1 >= 0:
                nums1[temp] = nums1[ptr1]
                temp -= 1
                ptr1 -= 1
            else:
                nums1[temp] = nums2[ptr2]
                temp -= 1
                ptr2 -= 1
            
