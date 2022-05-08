class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		noble = 0
		for x in A:
			# print('X :',x)
			less = 0
			for y in A:
				# print('Y :', y)
				if y > x:
					less += 1
			# print('Less:',less)
			if less == x:
				noble += 1
		# print('Noble:',noble)
		if noble > 0:
			return 1
		else:
			return -1


s = Solution()
print(s.solve([3, 2, 1, 3]))
print(s.solve([[1, 1, 3, 3]]))
