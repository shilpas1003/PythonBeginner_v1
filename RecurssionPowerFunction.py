import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B == 0:
            return 1 % C
        he = pow(A,(B//2),C)
        ha = ((he % C) * (he % C)) % C

        if B % 2 == 0:
            return ha
        return ((A % C) * (ha % C)) % C

s = Solution()
print(s.pow(2,3,3))
print(s.pow(0,0,1))