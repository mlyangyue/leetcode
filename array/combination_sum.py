#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
用递归的方式计算,用动态规划应该也可以,但是不太会:P
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.combination(candidates,target,0,[],res)
        return res

    def combination(self,nums,target,index,path,res):
        """

        :param nums:candidate numbers
        :param target: 目标值
        :param index: 查找起始未知
        :param path: 当前目标组合
        :param res: 最终结果集
        :return:
        """
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index,len(nums)):
            self.combination(nums,target-nums[i],i,path+[nums[i]],res)

if __name__ == "__main__":
    print Solution().combinationSum([2, 3, 6, 7],7)