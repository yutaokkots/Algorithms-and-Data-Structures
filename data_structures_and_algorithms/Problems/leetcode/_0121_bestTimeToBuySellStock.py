'''
121. Best Time to Buy And Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

from typing import List

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(0, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(profit, prices[i] - buy_price)
        return profit
    
    def maxProfit2(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_diff = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            max_diff = max(max_diff, prices[i] - min_price)
        return max_diff

    def maxProfit3(self, prices:list[int]) -> int:
        # return maximum value that can be achieved 
        # by iterating over prices list
        max_val = 0
        min_val = 10 ** 4
        max_index = 0
        min_index = 0

        # iterating over the prices list
        for index, price in enumerate(prices):
            # make sure that max_val proceeds the min_val
            # when price > max_val, then reassign price to max_val
            if price > max_val:
                max_val = price
                max_index = index
            # when price < min_val, then reassign price to min_val
            if price < min_val:
                min_val = price
                min_index = index

            if price > min_val and max_index < min_index:
                max_val = price 
                max_index = index

        return max_val - min_val 



questions = {
    "q1": [[7,1,5,3,6,4], 5],
    "q2": [[7,6,4,3,1], 0],
    "q3": [[1, 2, 3, 4, 5], 4],
    "q4": [[3, 3, 3, 3, 3], 0],
    "q5": [[5, 4, 3, 2, 1], 0],
    "q6": [[1, 1, 1, 1, 1], 0],
    "q7": [[2, 2, 2, 2, 2], 0],
    "q8": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9],
    "q9": [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0],
    "q10": [[2, 5, 7, 1, 4, 3, 6, 8], 7],
    "q11": [[3, 1, 4, 2, 5], 4],
    "q12": [[5, 2, 10, 1, 8], 8],
    "q13": [[4, 7, 2, 1, 11], 10],
    "q14": [[10, 1, 2, 3, 4, 5], 4],
    "q15": [[2, 4, 1, 5, 3], 4],
    "q16": [[5, 5, 5, 5, 5], 0],
    "q17": [[10, 7, 5, 8, 11, 9], 6],
    "q18": [[1, 2, 3, 4, 5, 4, 3, 2, 1], 4],
    "q19": [[5, 4, 3, 2, 1, 2, 3, 4, 5], 4],
    "q20": [[1, 2, 3, 2, 3, 4, 3, 4, 5], 4]
}

soln = Solution()
for k, v in questions.items():
    a = soln.maxProfit(v[0])
    print(f"{k}) q: {v[0]} a: {a} - {a == v[1]}")