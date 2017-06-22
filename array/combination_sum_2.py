#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'
"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
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
        if index >= len(nums):
            return
        for i in range(index,len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            self.combination(nums,target-nums[i],i+1,path+[nums[i]],res)



if __name__ == "__main__":
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5],8)