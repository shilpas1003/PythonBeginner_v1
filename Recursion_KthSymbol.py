import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, K):
        if N == 1 and K == 1:
            return 0

        mid = pow(2,N-1)//2
        # print(mid)
        if K <= mid:
            return self.solve(N-1,K)
        else:
            return 1 - (self.solve(N-1,K-mid))

s = Solution()
print(s.solve(2,2))
print(s.solve(2,1))