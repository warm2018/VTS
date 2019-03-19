import time

class Solution(object):
	def singleNumber(self,nums):
		a = 0
		for i in nums:
			a ^= i
			time.sleep(2)
			print(a)
		return a

if __name__ == '__main__':
	test = Solution()
	numberlist = [1,2,1,2,3,3,4]
	result = test.singleNumber(numberlist)
	print(result)
