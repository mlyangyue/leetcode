#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		i = 0  # nums1 下标
		j = 0  # nums2 下标
		array = []  # 新数组
		while i < len(nums1) or j < len(nums2):
			if i >= len(nums1):
				array.append(nums2[j])
				j += 1
			elif j >= len(nums2):
				array.append(nums1[i])
				i += 1
			else:
				if nums1[i] < nums2[j] :
					array.append(nums1[i])
					i += 1
				else:
					array.append(nums2[j])
					j += 1
		length = len(array)
		val = length%2
		if val == 1:
			return array,array[(length+1)/2-1]
		if val == 0:
			return array,(array[(length+2)/2-1]+array[length/2-1])/2.0


if __name__ == "__main__":
	print Solution().findMedianSortedArrays([1,2,5],[6])
