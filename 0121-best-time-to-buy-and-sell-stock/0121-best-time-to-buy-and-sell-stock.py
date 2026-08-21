class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        curr=prices[0]
        for price in prices:
            curr=min(curr,price)
            maxi=max(maxi,price-curr)
        return maxi
        