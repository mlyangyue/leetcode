#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
找出比当前值大的下一个排列
思路
1 原始数值"0125330"
2 从后面往前找到最长的 倒序 子串 '0125330' '5330'是最长的倒序子串
3 找到分割字符  '0125330' 2 为分割点
4 从后往前找出比 分割字符大的值并交换 "0135320"
5 交换剩下的 倒序子串 "0130235"
"""
class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		时间复杂度O(n)
		"""
		# 找最长倒序子串下标
		right = len(nums) - 1
		while nums[right] <= nums[right-1] and right >= 1:
			right -= 1
		if right == 0:
			self.reversed(nums, 0, len(nums)-1)
		# 找分割点,最长子串下标
		pivot = right - 1
		#找出大于分割点的值
		index = 0
		for i in range(len(nums)-1,pivot,-1):
			if nums[i] > nums[pivot]:
				index = i
				break
		#并交换
		nums[pivot], nums[index] = nums[index], nums[pivot]
		#交换后面的值
		self.reversed(nums,pivot+1,len(nums)-1)
		print nums





	def reversed(self,nums,l,r):
		while l < r:
			nums[l], nums[r] = nums[r], nums[l]
			l += 1
			r -= 1

if __name__ == "__main__":
	Solution().nextPermutation([3,2,1])