#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
"""


class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		m = 1
		for i, n in enumerate(nums):
			if i >= m:
				break
			m = max(m,i+n+1)
		return m >= len(nums)

if __name__ == "__main__":
	A = [3,2,1,0,4]
	print Solution().canJump(A)
