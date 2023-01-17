# https://leetcode.com/problems/the-kth-factor-of-n/description/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        t = factors(n)
        t.sort()
        print(t)
        if len(t) <= k-1:
            return -1
        return t[k-1]



def factors(n):    
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
