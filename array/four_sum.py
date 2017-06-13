#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		时间复杂度O(n^3)
		"""
		nums.sort()
		res_list = []
		for i in range(len(nums)):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			l = i + 1
			r = len(nums) - 1
			while l < r:
				l2 = l + 1
				r = len(nums) - 1
				if l > i+1 and nums[l] == nums[l-1]:
					l += 1
					continue
				while l2 < r:
					sumx = nums[i] + nums[l] + nums[l2] + nums[r]
					print i,l,l2,r
					if sumx == target:
						res_list.append([nums[i], nums[l], nums[l2], nums[r]])
						while l2 < r and nums[l2] == nums[l2+1]:
							l2 += 1
						while l2 < r and nums[r] == nums[r-1]:
							r -= 1
						l2 += 1
						r -= 1
					if sumx > target:
						r -= 1
					if sumx < target:
						l2 += 1
				l += 1
		return res_list

if __name__ == "__main__":
	print Solution().fourSum([0,0,0,0],0)

