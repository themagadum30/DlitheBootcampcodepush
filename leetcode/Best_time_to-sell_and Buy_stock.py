class Solution(object):
    def maxProfit(self, prices):
        mini = float('inf')
        maxi = 0
        for price in prices:
            if price < mini:
                mini = price
            profit = price - mini
            if profit > maxi:
                maxi = profit
        return maxi


        