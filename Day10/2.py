# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        # t = s.strip()
        p = s.split()
        # print(p)
        return " ".join(p[::-1])


        
        # print(t)

        # i=0
        # while t[i] == " " and t:
        #     t.pop(i)
        #     i += 1
        
        # j=len(t)-1
        # while t and t[j] == " ":
        #     t.pop()
        #     j-=1

        # print(t)
