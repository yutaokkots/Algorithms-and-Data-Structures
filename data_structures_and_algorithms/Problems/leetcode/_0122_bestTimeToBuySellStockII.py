'''
122. Best Time to Buy and Sell Stock II

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List

class Solution:
    """Solution class for LC0122."""

    def maxProfit(self, prices: List[int]) -> int:
        """Implementation of a greedy algorithm to determine max profit.

        Greedy algorithms focus on making the most beneficial decision 
        at every step, without considering the overall picture.
        In this problem, the buying and selling is repeated each day
        that there is an increase in stock price; profits are 
        accumulated for every time the stock price increases.

        Parameters
        ----------
        prices : List[int]
        """
        
        start_price = prices[0]
        max_value = 0
        for i in range(1, len(prices)):
            if prices[i] > start_price:
                max_value += prices[i] - start_price
            start_price = prices[i]

        return max_value