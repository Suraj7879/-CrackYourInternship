# https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

#Leetcode Equivalent: https://leetcode.com/problems/minimum-window-substring/submissions/875547922/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMap, window = {}, {}
        for i in range(len(t)):
            if t[i] not in hashMap:
                hashMap[t[i]] = 0
            hashMap[t[i]] += 1
        
        have, need = 0, len(hashMap)

        res, resLen = [-1, -1], 100000007

        l = 0

        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            
            if s[r] in hashMap and window[s[r]] == hashMap[s[r]]:
                have += 1

            while(have == need):
                if(r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                
                #Pop from the left of our window
                window[s[l]] -= 1
                if s[l] in hashMap and window[s[l]] < hashMap[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r+1]


            









        
        