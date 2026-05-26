class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')   # smallest price seen so far
        max_profit = 0             # best profit

        for price in prices:

            # update minimum buying price
            if price < min_price:
                min_price = price

            # calculate profit if selling today
            profit = price - min_price

            # update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit
        