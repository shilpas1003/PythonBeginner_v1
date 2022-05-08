class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        pow = 1
        ans = 0

        while(A):
            pow = pow * 5
            print('A pow:',A,pow)
            print('A ans :',A,ans)
            if A & 1:
                ans += pow
            A >>= 1
        return ans

s = Solution()
print(s.solve(5))