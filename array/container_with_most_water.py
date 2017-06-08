#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
找到一组线段中，最合适的两条线段，使得它俩和X轴组成的桶子能装最多的水。短板决定装水的多少
"""
class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		i = 0
		j = len(height) - 1
		max_area = 0
		while i < j:
			max_area = max(max_area, (j-i)*min(height[j],height[i]))
			if height[i]<height[j]:
				i += 1
			else:
				j -= 1

		return max_area

if __name__ == "__main__":
	print Solution().maxArea([1,2,4,3])
