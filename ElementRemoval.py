class Solution:
    def min_cost(self,A):
        desc = sorted(A,reverse=True)
        total = 0
        for i,x in enumerate(desc):
            total += (i+1) * x
        return total
s = Solution()
# print(s.min_cost([5]))
print(s.min_cost([8,0,10]))