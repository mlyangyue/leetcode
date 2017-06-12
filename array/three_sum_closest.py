#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
	For example, given array S = {-1 2 1 -4}, and target = 1.
	The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
找到3个数的和 最接近目标值 和three_sum很像
"""
class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		时间复杂度O(N^2)
		"""
		nums.sort()
		res = nums[0] + nums[1] + nums[2]
		for i in range(len(nums) - 2):
			j = i + 1
			k = len(nums) -1
			while j < k:
				sum = nums[i] + nums[j] + nums[k]
				if sum == target:
					return sum
				if abs(sum - target) < abs(res - target):
					res = sum
				if sum < target:
					j += 1
				else:
					k -= 1
		return res


if __name__ == "__main__":
	print Solution().threeSumClosest([0,2,1,-3],1)
