#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		res = []
		count = 0
		while matrix:
			res.extend(matrix.pop(0))
			if matrix and matrix[0]:
				for item in matrix:
					res.append(item.pop(-1))
			if matrix:
				res.extend(matrix.pop(-1)[::-1])
			if matrix and matrix[0]:
				for item in matrix[::-1]:
					res.append(item.pop(0))
		return res


if __name__ == '__main__':
	m = [
		[3],
		[6],
		[9]
	]
	print Solution().spiralOrder(m)
