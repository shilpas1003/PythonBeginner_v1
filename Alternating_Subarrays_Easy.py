class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        length = 2 * B + 1
        center = []

        for start in range(n - length + 1): # l = e - s + 1
            end = start + length - 1

            #validating sequence
            prev = None
            is_alternating = True
            for i in range(start,end + 1):
                if A[i] == prev:
                    is_alternating = False
                    break
                prev = A[i]

            if is_alternating:
                center.append((start + end) // 2)
        return center
    def solve2(self,A,B):
        n = len(A)
        length = 2 * B + 1
        center = []
        s = 0
        prev = None
        while s < (n - length + 1):
            e = s + length - 1
            if s == 0:
                if A[e] == prev:
                    return e


s = Solution()
print(s.solve2([1, 0, 1, 0, 1],1))
print(s.solve([0, 0, 0, 1, 1, 0, 1],0))