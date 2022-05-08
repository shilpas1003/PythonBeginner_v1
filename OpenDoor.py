class Solution:
    # @param A : tuple of integers
    # @return an integer
    def OpenDoor_BruteForce(self, N):

        A = [False] * N #Extra Space
        for i in range(1,N+1):
            for j in range(i,N+1,i):
                A[j-1] = not A[j-1]
        print(A)
        count = 0
        for x in A:
            if x:
                count += 1
        return count

    def OpenDoor_Optimised(self,N):
        c = 0
        i = 1
        while i * i <= N:
            # print(i)
            c = c + 1
            i = i + 1
        return c

s = Solution()
print(s.OpenDoor_BruteForce(5))
print(s.OpenDoor_Optimised(100))
