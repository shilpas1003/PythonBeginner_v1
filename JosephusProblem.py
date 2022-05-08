class Solution:
    # @param A : tuple of integers
    # @return an integer
    def Josephus_BruteForce(self, A):
        n = len(A)
        positions = []

        for i in range(1,n+1):
            positions.append(i)
        print('Initial Position :',positions)

        killerPosition = 0
        victimPosition = 1
        # m = len(positions)
        # print(m)
        while len(positions) != 1:
            print('killer position who has sword :', killerPosition, ' &&&& vicitim position :', victimPosition,'length of Position array :',len(positions))
            if killerPosition < (len(positions)-2) :
                victimPosition = killerPosition + 1
                killerPosition = victimPosition
            elif killerPosition == (len(positions)-2) : #killer is 2nd last
                victimPosition = killerPosition + 1
                killerPosition = 0
            elif killerPosition == (len(positions)-1):
                victimPosition = 0
                killerPosition = victimPosition
            positions.pop(victimPosition)
            # print(victimPosition)
        surviving_position = positions[0]
        return surviving_position

s = Solution()
print(s.Josephus_BruteForce((1,2,3,4,5)))