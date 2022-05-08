class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    #BruteForce Solution with TC = O(n * Q) & SC = O(Q)
    def solve(self, A, B):
        ans = []
        Q = len(B)
        n = len(A)
        for q in range(0,Q):
            sum = 0
            for i in range(0,n):
                sum = sum + A[i]
                if sum > B[q]:
                    ans.append(i)
                    break
            if sum <= B[q]:
                ans.append(n)
        return ans
    def upperbound(self,A,B):
        n = len(A)
        start = 0
        end = n - 1
        ans = -1
        target = B
        count = 0
        while start<=end:
            mid = (start + end) // 2
            print('start:',start)
            print('end:',end)
            print('mid',mid)
            #case 1 : found Target Number
            print('A[mid]: ',A[mid],'target :',target,'count :',count)
            if B < A[0]:
                return 0

            if B > A[n- 1]:
                return n


            if A[mid]  < target:
                start = mid+1
                count += 1
                # break
                #case 2 : Mid number is greater than target then search in left part
            if A[mid] == target:
                return count + 1
            elif A[mid] > target:
                end = mid -1
        return count

    def solve1(self,A,B):
        p = [A[0]]
        # for x in A[1:]:
        #     p.append(x,p[-
        n = len(A)
        g = len(B)
        p = [A[0]]
        ans = []
        for x in A[1:]:
            p.append(x + p[-1])
        print(p)
        if n == g:
            for s in range(n):
                max = B[s]
                count = 0
                # print(max)
                for e in range(s,n):
                    if max < p[e]:
                        # print(e,end=',')
                        count = count + 1
        print(count,end=',')


s = Solution()
print(s.solve1([3, 4, 4, 6],[20, 4 , 10, 2]))
