import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A % 9 == 1:
            return 1
        else:
            return 0

s = Solution()
print(s.solve(83557))
print(s.solve(1291))
print(s.solve(291529))
