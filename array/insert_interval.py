#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[Interval]
		:type newInterval: Interval
		:rtype: List[Interval]
		"""
		s = newInterval.start
		e = newInterval.end
		left = [i for i in intervals if i.end < s]
		right = [i for i in intervals if i.start > e]
		if left + right != intervals:
			s = min(s,intervals[len(left)].start)
			e = max(e,intervals[-len(right)-1].end)
		return left + [Interval(s,e)] + right


if __name__ == "__main__":
	l = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
	args = []
	for it in l:
		args.append(Interval(it[0], it[1]))

	new = Interval(4, 9)
	ret = Solution().insert(args, new)
	t_list = []
	for item in ret:
		t_list.append([item.start, item.end])
	print t_list
	print