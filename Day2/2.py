# https://www.geeksforgeeks.org/chocolate-distribution-problem/

#User function Template for python3

# def backtrack(nums, op, res, M):
#     if(len(nums) == 0):
#         if len(op) == M:
#             res.append(op)
#         return
#     op1 = op[:]
#     op2 = op[:]
#     op2.append(nums[0])
#     nums = nums[1:]
#     backtrack(nums, op1, res, M)
#     backtrack(nums, op2, res, M)

class Solution:
    def findMinDiff(self, A,N,M):
        # using finding all subset technique, resulting in TLE
        # res = []
        # temp = 1000
        # backtrack(A, [], res, M)
        # for i in range(len(res)):
        #     if (len(res[i]) == M):
        #         mn = min(res[i])
        #         mx = max(res[i])
        #         t = mx - mn
        #         temp = min(temp, t)
        # return temp
        
        #Using sliding window technique by sorting the array O(NlogN) solution
        A.sort()
        temp = A[N-1] - A[0]
        for i in range(N-M+1):
            nums = A[i+M-1] - A[i]
            temp = min(nums, temp)
        return temp
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends