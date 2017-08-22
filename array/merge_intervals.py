#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
求交集,无序
"""


# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		if not intervals:return []
		ret_list = [intervals[0]]
		for i in range(1,len(intervals)):
			interval_i = intervals[i]
			j = 0
			while j < len(ret_list):
				interval_j = ret_list[j]
				if interval_i.start>interval_j.end or interval_i.end < interval_j.start:
					j += 1
					continue
				interval_i.start = min(interval_j.start,interval_i.start)
				interval_i.end = max(interval_j.end,interval_i.end)
				ret_list.pop(j)
			ret_list.append(interval_i)

		return ret_list


if __name__ == "__main__":
	l = [[2,3],[4,5],[6,7],[8,9],[1,10]]
	args = []
	for it in l:
		args.append(Interval(it[0],it[1]))

	ret = Solution().merge(args)
	t_list = []
	for item in ret:
		t_list.append([item.start,item.end])
	print t_list
