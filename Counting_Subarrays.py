class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 0
        end = 0
        count = 0
        sum = A[0]
        n = len(A)
        while (start < n and end < n):
            if (sum < B):
                end += 1

                if (end >= start):
                    count += end - start

                if (end < n):
                    sum += A[end]
            else:
                sum -= A[start]
                start += 1

        return count

s = Solution()
print(s.solve([ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3, 4, 4, 5, 2, 2, 4, 9, 8, 5 ],32))