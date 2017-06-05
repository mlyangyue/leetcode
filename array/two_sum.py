#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import unittest


class Solution(object):
	def twoSum(self, nums, target):
		"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		if len(nums) <= 1:
			return False
		temp_dict = {}
		for i, num in enumerate(nums):
			value = target - num
			if num not in temp_dict:
				temp_dict[value] = i
			else:
				return [temp_dict[num], i]


class mytest(unittest.TestCase):
	def setUp(self):
		self.tclass = Solution()

	def tearDown(self):
		pass

	def testtwosum(self):
		self.assertEqual(self.tclass.twoSum([1,2,3,4,5],6),[1,3])


if __name__ == "__main__":
	unittest.main()