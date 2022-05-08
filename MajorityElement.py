class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement1(self, A):
        #BruteForce Approach
        N = len(A)
        for x in A:
            frequency = 0
            for y in A:
                if x == y:
                    frequency += 1
            if frequency > (N/2):
                return x

    # def majorityElement(self, A):
        # N = len(A)
        # for i in range(N):
        #     for j in range(N-1):
        #         if A[j] > A[j+1]:
        #             A[j],A[j+1] = A[j+1],A[j]
        # # print(A)
        # curr = A[0]
        # freq = 0
        # if N <= 1:
        #     return curr
        # else:
        #     for i in range(1,N):
        #         if A[i] == curr:
        #             freq += 1
        #             # print(freq)
        #             if (freq + 1) > (N/2):
        #                 return A[i]
        #         else:
        #             curr = A[i]
        #             freq = 0

s = Solution()
print(s.majorityElement([2, 1, 2]))
# print(s.majorityElement1([2, 1, 2]))
print(s.majorityElement([3,4,3,6,1,3,2,5,3,3,3]))
# print(s.majorityElement1([3,4,3,6,1,3,2,5,3,3,3]))
print(s.majorityElement([100]))
print(s.majorityElement([ 2, 1, 1 ]))