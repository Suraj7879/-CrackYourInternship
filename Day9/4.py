# https://leetcode.com/problems/valid-palindrome-ii/
# Time: O(N), Space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                t1 = isPalindrome(s[left+1: right+1])
                t2 = isPalindrome(s[left: right])
                return t1 or t2
        return True

def isPalindrome(s):
    print(s)
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


        # flag = 0
        # while left < right:
        #     print(left, end=" ")
        #     print(right)
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     elif s[left] == s[right-1]:
        #         right -= 1
        #         flag += 1
        #         if flag > 1:
        #             print("2")
        #             return False
        #     elif s[left+1] == s[right]:
        #         left += 1
        #         flag += 1
        #         if flag > 1:
        #             print("1")
        #             return False
        #     else:
        #         print("3")
        #         return False
        # return True