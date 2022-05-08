class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0 or A == 1:
            return 1
        return self.solve(A - 1) * A

s = Solution()
print(s.solve(4))
print(s.solve(1))
