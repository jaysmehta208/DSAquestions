'''
Problem statement
You are given an array of integers 'prices' of size 'n', where ‘prices[i]’ is the price of a given stock on an ‘i’-th day.
You want to maximize the profit by choosing a single day to buy one stock and a different day to sell that stock.
Please note that you can’t sell a stock before you buy one.
Return the maximum profit you can achieve from this transaction.

Example :
Input: ‘prices’ =[7, 1, 5, 4, 3, 6]
Output: 5
Explanation: Purchase stock on day two, where the price is one, and sell it on day six, where the price is 6, profit = 6 - 1 = 5.
Hence we return 5.
'''

from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minbefore = prices[0]
        for i in range(1,len(prices)):
            if (prices[i] - minbefore > maxprofit):
                maxprofit = prices[i] - minbefore
            if (prices[i] < minbefore):
                minbefore = prices[i]
        return maxprofit
    
# Time complexity: O(n)
# Space complexity: O(1)