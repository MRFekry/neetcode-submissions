class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lbuy, rsell = 0, 1
        maxProfit = 0
        while rsell < len(prices):
            if rsell == lbuy:
                rsell += 1
            elif prices[lbuy] <= prices[rsell]:
                profit = prices[rsell] - prices[lbuy]
                if maxProfit < profit:
                    maxProfit = prices[rsell] - prices[lbuy]
                rsell += 1
            else:
                lbuy += 1
        return maxProfit