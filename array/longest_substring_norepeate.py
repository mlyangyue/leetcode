#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_len = 0
		start = 0
		temp_dict = {}
		for i in range(len(s)):
			if s[i] in temp_dict and start <= temp_dict[s[i]]: #如果在字典里并且start小于等于上一次重复的字符下标
				start = temp_dict[s[i]] + 1  # 找到上次重复的下标
			else:
				max_len = max(max_len, i - start + 1) # 最大值 和 当前下标到上次重复的距离 做比较
			temp_dict[s[i]] = i
		return max_len

if __name__ == "__main__":
	print Solution().lengthOfLongestSubstring('dvdfe')