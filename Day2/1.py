# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


#BruteForces, O(n^2) solution (Getting TLE on Leetcode)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                cost = prices[j] - prices[i]
                maxi = max(maxi, cost)
        return maxi

#Time: O(n), Space: O(1)
#DP Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = prices[i] - mini
            profit = max(profit, cost)
            mini = min(mini, prices[i])
        return profit

