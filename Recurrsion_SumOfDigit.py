import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        rem = A % 10
        return rem + self.solve((A // 10))

s = Solution()
print(s.solve(46))
print(s.solve(11))
print(s.solve(83557))