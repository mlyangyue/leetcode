#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
	def searchRange_v1(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		start = -1
		end = start
		for i in range(len(nums)):
			if nums[i] != target:
				continue
			if start == -1:
				start = i
				end = i
			if start != -1:
				end = i

		return [start, end]

	def searchRange_v2(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		二分法查找
		"""
		def binary_search_left(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) / 2
				if target > nums[mid]:
					left = mid + 1
				else:
					right = mid - 1
			return left
		def binary_search_right(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) / 2
				if target >= nums[mid]:
					left = mid + 1
				else:
					right = mid - 1
			return right
		left = binary_search_left(nums, target)
		right = binary_search_right(nums, target)
		return (left,right) if left <= right else [-1,-1]


if __name__ == '__main__':
	print Solution().searchRange_v2([10,10,10],10)