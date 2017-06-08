#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
"""
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		时间复杂度O(n^2)
		这个是我的算法
		"""
		max_len = 0
		string = ""
		temp_str = ""
		length = len(s)
		for i in range(length):
			n = 0
			flag = False
			while s[i-n] == s[i+n]:
				n += 1
				flag = True
				if i+n > length - 1 :
					break
				if i-n <0:
					break
			if flag:
				temp_str = s[i-n+1:i+n] if n != 0 else s[i]
				max_len = max(max_len,len(temp_str))
				string = string if max_len > len(temp_str) else temp_str
			n = 0
			flag = False
			while i<length-1 and s[i-n] == s[i+n+1]:
				n += 1
				flag = True
				if i+n+1 > length -1:
					break
				if i-n < 0:
					break
			if flag:
				temp_str = s[i-n+1:i+n+1]
				max_len = max(max_len,len(temp_str))
				string = string if max_len > len(temp_str) else temp_str
		return string


	def longestPalindromev2(self, s):
		"""
		:type s: str
		:rtype: str
		时间复杂度O(n)
		这个是leetcode上别人的算法,好腻害
		"""
		max_len = 1
		start = 0
		for i in range(len(s)):
			if i-max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]: # 'babab'
				start = i-max_len-1
				max_len += 2
				continue
			if i-max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]: # 'cbbd'
				start = i-max_len
				max_len += 1
		return s[start:start+max_len]
if __name__ == '__main__':
	s = 'cbbd'
	print Solution().longestPalindrome(s) # 时间复杂度 O(n^2)
	print Solution().longestPalindromev2(s) # 时间复杂度 O(n)