#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
动态规划 max(arr[n-1]+arr[n],arr[n])

"""


class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		cur = 0
		res = ""
		for num in nums:
			if res == "":
				res = num
			cur = max(num + cur, num)
			res = max(res, cur)

		return res


if __name__ == "__main__":
	print Solution().maxSubArray([1, -2, 3, 10, -4, 7, 2, -5])
