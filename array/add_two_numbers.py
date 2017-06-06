#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		curnode = ListNode(0)
		newnode = curnode
		cur = 0
		while l1 or l2 or cur:
			v1 = 0
			v2 = 0
			if l1:
				v1 = l1.val
				l1 = l1.next
			if l2:
				v2 = l2.val
				l2 = l2.next
			res = v1+v2+cur
			cur = res // 10
			val = res % 10
			curnode.next = ListNode(val)
			curnode = curnode.next
		return newnode.next


if __name__ == "__main__":
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(7)
	newnode = Solution().addTwoNumbers(l1,l2)
	while newnode:
		print newnode.val
		newnode = newnode.next