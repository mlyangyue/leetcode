#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
思路:先排序,左右各一个指针, nums[left] + nums[i] + nums[right] > 0 right-=1  nums[left] + nums[i] + nums[right]<0 left+=1
优化 如果第i个值和第i-1个值相等 跳过循环, 如果left值和left+1值相等 跳过循环,right和right-1值相等,跳过循环
"""
class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		时间复杂度O(n^2)
		"""
		nums = sorted(nums)
		res_list = []
		for i in range(len(nums)):
			if i > 0 and nums[i]==nums[i-1]:
				continue
			left = i + 1
			right = len(nums) - 1
			while left < right:
				sum = nums[left] + nums[i] + nums[right]
				if i == 1:
					print nums[left],nums[i],nums[right]
				if sum == 0:
					res_list.append([nums[left], nums[i], nums[right]])
					while left < right and nums[left] == nums[left+1]:
						left += 1
					while left < right and nums[right] == nums[right-1]:
						right -= 1
					right -= 1
					left += 1
				elif sum > 0:
					right -= 1
				elif sum < 0:
					left += 1
		return res_list


if __name__ == "__main__":
	print Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])