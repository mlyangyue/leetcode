#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        O(n)
        """
        length = len(nums)
        start = 0
        for i in range(length):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        return start
if __name__ == '__main__':
    print Solution().removeElement([3,2,2,3],3)