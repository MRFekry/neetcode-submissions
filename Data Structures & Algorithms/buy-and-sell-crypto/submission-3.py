class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, profit = 0, 0
        while left < len(prices):
            right = left + 1
            while right < len(prices) and prices[right] > prices[left]:
                diff = prices[right] - prices[left]
                if diff > profit:
                    profit = diff
                right += 1
            left += 1
        return profit
         