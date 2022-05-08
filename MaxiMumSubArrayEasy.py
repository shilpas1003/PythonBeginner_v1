class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        maxSum = -float('inf')
        n = len(C)
        for s in range(n):
            for e in range(s,n):
                sum = 0
                for i in range(s,e+1):
                    sum += C[i]
                    if sum > maxSum and sum <= B:
                        maxSum = sum
        return maxSum

    def maxSubarray1(self,A,B,C):
        maxSum = -float('inf')
        n = len(C)
        for s in range(n):
            sum = 0
            for e in range(s, n):
                # print(s,e)
                sum += C[e]
                if sum > maxSum and sum <= B:
                    maxSum = sum
        if maxSum == -float('inf'):
            return 0
        else:
            return maxSum

    def NumOfSubArray(self,A,B):
        n = len(A)
        count = 0
        for s in range(n):
            sum = 0
            for e in range(s, n):
               sum += A[e]
               if sum <= B:
                count += 1
        return count

s = Solution()
# print(s.maxSubarray(5,12,[2, 1, 3, 4, 5]))
# print(s.maxSubarray1(5,12,[2, 1, 3, 4, 5]))
# print(s.maxSubarray1(3,1,[2,2,2]))
print(s.NumOfSubArray([2,5,6,6],10))
print(s.NumOfSubArray([1,11,2,2,3,15],10))
print(s.NumOfSubArray([ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3, 4, 4, 5, 2, 2, 4, 9, 8, 5 ],32))