# https://leetcode.com/problems/palindrome-number/submissions/876888378/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != abs(x):
            return False

        leftPtr = 0
        rightPtr = len(str(x))-1
        y = str(x)
        while leftPtr <= rightPtr:

            if y[leftPtr] != y[rightPtr]:
                return False
            
            leftPtr += 1
            rightPtr -= 1

        return True
                
