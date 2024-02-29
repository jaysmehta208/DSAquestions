# coding ninja solution
'''
Problem statement
Given an array 'v' of 'n' numbers.



Your task is to find and return the highest and lowest frequency elements.


If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.



Example:
Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]

Output: 1 2

Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].
'''

from typing import List
import sys
def getFrequencies(v: List[int]) -> List[int]: 
    d = {}
    for i in v:
        d[i] = d.get(i, 0) + 1
    mini = sys.maxsize
    mini2 = sys.maxsize
    freq = 0 
    freq2 = sys.maxsize
    
    for i in d:
        if (d[i] > freq):
            freq = d[i]
        if (d[i] < freq2):
            freq2 = d[i]
    for i in d:
        if d[i] == freq and i < mini:
            mini = i
        if d[i] == freq2 and i < mini2:
            mini2 = i
    l = [mini, mini2]
    return l

