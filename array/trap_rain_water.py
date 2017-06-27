#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""


class Solution(object):
	def trap(self, arr):
		"""
        :type height: List[int]
        :rtype: int
        没想出来,参考的网上的解决方案.很好的思路
        """
		height, left, right, water = [], 0, 0, 0
		for i in arr:
			left = max(left, i)
			height.append(left)
		height.reverse()
		for n, i in enumerate(reversed(arr)):
			right = max(right, i)
			water += min(height[n], right) - i
		return water


if __name__ == "__main__":
	print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
