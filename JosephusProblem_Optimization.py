class Solution:
    # @param A : tuple of integers
    # @return an integer
    def Josephus_Optimized(self, A):
        i = 1
        while i <= A:
            i = i * 2
            print(i)
        i = i // 2
        print('division :',i)

        killed = A - i
        return (2 * killed) + 1

s = Solution()
print(s.Josephus_Optimized(100))