#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""
# 思路:1.初始化存储字符容器,2,正序竖行, i==numRows-1时,逆序存储,等到标记i=0时再切换正序,如此反复

def convert(s, numRows):
    temp = [""]*numRows
    flag = -1
    i = 1
    if numRows==1 or len(s)<numRows:
        return s
    for w in s:
        i = i + flag
        temp[i] += w
        if i == numRows-1:
            flag=-1
        if i == 0:
            flag = 1
    return ''.join(temp)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    r = convert("PAYPALISHIRING",3)
    print r=='PAHNAPLSIIGYIR' # True