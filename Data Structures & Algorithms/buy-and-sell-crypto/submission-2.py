class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=prices[0]
        m=0
        for i in range(len(prices)):
            if prices[i]<l:
                l=prices[i]
            elif prices[i]-l>m:
                m=prices[i]-l
            
        return m