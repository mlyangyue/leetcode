#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
旋转数组查找,有序，本能想到用二分查找
思路:
获取数组元素的分割点,时间复杂度为O(log(n))
比较待查找元素与第一个元素，如果待查找元素大于等于第一个元素，表明待查找元素在前半段有序数组中；如果不是这待查找元素在后半段数组中
判断待查找元素所在的有序数组以后,用二分查找找出元素位置
"""

class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return -1
		right = len(nums)-1
		left = 0
		while left <= right:
			middle = left + (right - left)/2
			if nums[middle] == target:
				return middle
			elif nums[middle] >= nums[left]:
				if target >= nums[left] and nums[middle] > target:
					right = middle - 1
				else:
					left = middle + 1
			elif nums[middle] < nums[left]:
				if target <= nums[right] and nums[middle] < target:
					left = middle + 1
				else:
					right = middle - 1
		return -1
if __name__ == '__main__':
	print Solution().search([1,3,5],1)



