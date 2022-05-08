class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        n = len(A)
        sum = 0
        for s in range(n):
            for e in range(s,n):
                for i in range(s,e+1):
                    sum += A[i]
        return sum

    def subarraySum2(self,A):
        n = len(A)
        prefix = [A[0]]
        for x in A[1:]:
            prefix.append(x + prefix[-1])
        # print(prefix)
        sum = 0
        for s in range(n):
            # print('sum in start loop:',sum)
            for e in range(s,n):
                # print(s,e)
                if s == 0:
                    sum += prefix[e]
                else:
                    sum += prefix[e] - prefix[s-1]
                # print('sum :',sum)
        return sum
    def subarraySum3(self,A):
        n = len(A)
        sum = 0
        for i in range(n):
            sum += A[i] * (n - i) * (i +1)
        return sum
    def subarraySum4(self,A,B,C):
        n = len(C)
        sum = 0
        for i in range(n):
            if sum != B:
                sum += C[i] * (n - i) * (i +1)
        return sum
s = Solution()
# print(s.subarraySum3([1, 2, 3]))
# print(s.subarraySum3 ([2,1,3]))
print(s.subarraySum4(5,12,[2, 1, 3, 4, 5]))