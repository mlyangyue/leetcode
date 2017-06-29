#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
"""


class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        先倒序,然后交换位置
		"""
		matrix.reverse()
		print matrix
		for i in range(len(matrix)):
			for j in range(i + 1, len(matrix[i])):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
	a = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
	print a
	Solution().rotate(a)
	print a
