# Final prices with special discount in a shop problem: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        
        for i in range(0, length):
            for j in range(i + 1, length):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        
        return prices
