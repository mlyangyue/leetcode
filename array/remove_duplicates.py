#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
Subscribe
"""
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		时间复杂度O(n)
		"""
		if len(nums) == 0:
			return 0
		length = 0
		for i in range(1,len(nums)):
			if nums[i] != nums[length]:
				length += 1
				nums[length] = nums[i]
		return length + 1

if __name__ == "__main__":
	l = [1,1]
	print Solution().removeDuplicates(l)