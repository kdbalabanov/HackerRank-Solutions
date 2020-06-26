# Best Time to Buy and Sell Stock problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = float('inf')
        profit = 0
        
        for price in prices:
            cost, profit = min(cost, price), max(profit, price - cost)
            
        return profit