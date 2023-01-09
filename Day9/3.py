# https://leetcode.com/problems/longest-common-prefix/
# Time: O(N^2), Space: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenn = len(strs[0])
        idx = 0
        for i in range(1, len(strs)):
            minn = len(strs[i])
            if minn < lenn:
                lenn = minn
                idx = i
        
        longestL = 0
        for i in range(lenn):
            item = strs[idx][i]
            for j in strs:
                if j[i] == item:
                    continue
                else:
                    return strs[0][:longestL]
            longestL += 1
        return strs[0][:longestL]