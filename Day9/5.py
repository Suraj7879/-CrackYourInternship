# https://leetcode.com/problems/integer-to-roman/
# Time: O(N), Space: O(1)


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        mapp = [["I", 1],["IV", 4],["V", 5],["IX", 9],["X", 10],["XL", 40],["L", 50],["XC", 90],["C", 100],["CD", 400],["D", 500],["CM", 900],["M", 1000]]
        i = len(mapp) - 1
        while num:
            res += (num//mapp[i][1]) * mapp[i][0]
            num %= mapp[i][1]
            i -= 1
        return res
