#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
Subscribe to see which companies asked this question.
"""
class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		我没想出来,看的leetcode上的Solution
		"""
		nums.append(0)
		n = len(nums)
		for i in range(n):
			if nums[i] < 0 or nums[i] >= n:
				nums[i] = 0
		for i in range(n):
			nums[nums[i]%n] += n

		for i in range(1,n):
			if nums[i]/n == 0:
				return i
		return n

if __name__=="__main__":
	print Solution().firstMissingPositive([2,2])