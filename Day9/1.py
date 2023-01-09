# https://leetcode.com/problems/valid-parentheses/
# Time: O(n), Space: O(1)
class Solution:
    def isValid(self, s: str) -> bool:
        openBr = ['(', '{', '[']
        stack = []

        for i in range(len(s)):
            if s[i] in openBr:
                stack.append(s[i])
            else:
                if s[i] is '}' and stack and stack[len(stack)-1] is '{':
                    stack.pop()
                elif s[i] is ']' and stack and stack[len(stack)-1] is '[':
                    stack.pop()
                elif s[i] is ')' and stack and stack[len(stack)-1] is '(':
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
