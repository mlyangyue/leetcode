#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
有序数组查找用用二分法查找
"""
class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return 0
		if nums[-1] < target:
			return len(nums)
		l = 0
		r = len(nums) - 1
		while l <= r:
			m = (l + r)/2
			if nums[m] == target:
				return m
			if nums[m] > target:
				r = m - 1
				if r >= 0:
					if nums[r] < target:
						return r + 1
				else:
					return 0
			else:
				l = m + 1
				if l < len(nums):
					if nums[l] > target:
						return l
					else:
						return len(nums)

if __name__ == "__main__":
	print Solution().searchInsert([1,3,5,6],7)



