# https://leetcode.com/problems/simplify-path/
# Time: O(N), Space: O(1)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        x = path.split("/")
        for i in x:
            if stack and i == "..":
                stack.pop()
            elif i not in [".", "", ".."]:
                stack.append(i)
        print(stack)
        return "/" + "/".join(stack)
