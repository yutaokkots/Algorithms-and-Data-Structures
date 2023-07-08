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