class Solution:
    def solve(self, A, B):
        n = len(A)
        dp = [0] * (n+1)
        for i in range(n):
            dp[i+1]=dp[i]+A[i]
        ans = 0
        print(dp)
        for i in range(n):
            for j in range(i,n):
                sum = dp[j+1]-dp[i]
                sz = j-i+1
                if sz%2==0 and sum<B: ans+=1
                if sz&1 and sum>B: ans+=1
        return ans

    def check(self,n):
        if n & 1:
            return True
        else:
            return False
s = Solution()
print(s.solve([1, 2, 3, 4, 5],4))
print(s.check(4))