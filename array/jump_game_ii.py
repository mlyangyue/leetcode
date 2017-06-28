#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        贪婪算法
        """
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1 #每次一个step
            maxend = end + 1
            for i in range(start, end + 1):
                # 超出结尾 返回step
                if i + nums[i] >= n - 1:
                    return step
                # 每次得到当前下标到移动后的下标和上次的下标值做比较
                maxend = max(maxend, i + nums[i])
            # 找到最大值,移动下标
            start, end = end + 1, maxend
        return step

if __name__ == "__main__":
    print Solution().jump([2,3,1,1,4,8,2,3,1])

