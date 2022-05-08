class Solution:
    # @param A : list of integers
     # @return an long
    def MinMaxSubArray(self, A):
        minVal = min(A)
        maxVal = max(A)

        iMin = None
        iMax = None
        minlen = float('inf')

        for i in range(len(A)):
            if A[i] == minVal:
                iMin = i
                if iMax is not None:
                    length = iMin - iMax + 1
                    minlen = min(length,minlen)
            if A[i] == maxVal:
                iMax = i
                if iMin is not None:
                    length = iMax - iMin + 1
                    minlen = min(length,minlen)

        return minlen
s = Solution()
print(s.MinMaxSubArray([2,-1,6,8,-1,3,0,8,0,8,2,-1]))
