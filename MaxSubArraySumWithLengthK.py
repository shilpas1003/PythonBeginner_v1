class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A,K):
        maxSum = -float('inf')
        n = len(A)
        for s in range(n-K+1):
            e = s + K-1
            sum = 0
            for i  in range(s,e+1):
                sum += A[i]
            maxSum = max(sum,maxSum)
        return maxSum

    def solve1(self,A,K):
        n = len(A)
        prefix =[A[0]]
        for x in A[1:]:
            prefix.append(x + prefix[-1])

        print(prefix)
        maxSum = -float('inf')
        n = len(A)
        for s in range(n - K + 1):
            e = s + K - 1
            if s == 0:
                sum = prefix[e]
            else:
                sum = prefix[e] - prefix[s-1]
            # print(sum)
            maxSum = max(maxSum,sum)
        return maxSum

    def solve2(self,A,K):
        #Moving Window
        sum = 0
        n = len(A)
        maxSum = -float('inf')
        for i in range(K):
            sum += A[i]
        maxsum = sum
        for s in range(1,n-K+1):
            e = s + K - 1
            sum = sum - A[s-1] + A[e]
            maxsum = max(maxsum,sum)
        return maxSum
s= Solution()
print(s.solve([3, 7, 90, 20, 10, 50, 40],3))
print(s.solve1([3, 7, 90, 20, 10, 50, 40],3))
print(s.solve2([3, 7, 90, 20, 10, 50, 40],3))