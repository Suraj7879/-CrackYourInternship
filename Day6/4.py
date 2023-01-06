# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

#Using prefix sum array
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        forwardPrefixSum = [None] * len(cardPoints)
        backwardPrefixSum = [None] * len(cardPoints)

        summ = 0
        for i in range(len(cardPoints)):
            summ += cardPoints[i]
            forwardPrefixSum[i] = summ
        
        reversedCardPoints = cardPoints[::-1]
        summ = 0
        for i in range(len(cardPoints)):
            summ += reversedCardPoints[i]
            backwardPrefixSum[i] = summ
        
        maxx = max(forwardPrefixSum[k-1], backwardPrefixSum[k-1])
        for i in range(1, k):
            temp = k - i
            t1 = forwardPrefixSum[i-1]
            t2 = backwardPrefixSum[temp-1]
            print(t1, end=" ")
            print(t2)
            summ = t1 + t2
            maxx = max(maxx, summ)
        
        return maxx






