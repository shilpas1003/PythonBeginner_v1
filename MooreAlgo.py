class Solution:
    # @param A : tuple of integers
    # @return an integer
    def MooreAlgo(self, A):
        n = len(A)
        # current = A[0]
        ME = A[0]
        freq = 1
        for i in range(1,n):
            if ME != A[i] and ME != None:
                ME = None
                freq = freq - 1
            else:
                ME = A[i]
                freq = freq + 1
        moore1 = ME
        # print('moor1',moore1)
        #edge Case
        current = A[0]
        freq1 = 0
        moore2 = 0
        for i in range(1,n):
            # print('current', current,'i:',i)
            if current == A[i]:
                freq1 += 1
                # print('freq1:',freq1)
                if freq1 > (n/2):
                    moore2 = current
            else:
                current = A[i]
        # print('moor2',moore2)
        if moore1 == moore2:
            return moore1

s = Solution()
print(s.MooreAlgo([ 2, 1, 1,1,1]))
print(s.MooreAlgo([4,6,5,3,4,5,6,4,4,4]))
print(s.MooreAlgo([3,4,3,6,1,3,2,5,3,3,3]))
