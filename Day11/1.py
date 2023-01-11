# https://leetcode.com/problems/group-anagrams/description/
# Time:O(Nklogn) , Space: O(N)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []
        for i in strs:
            temp = sorted(i)
            temp = ''.join(temp)
            if temp not in hashMap:
                hashMap[temp] = []
            hashMap[temp].append(i)
        
        for i in hashMap:
            output.append(hashMap[i])
        
        return output
        
        

