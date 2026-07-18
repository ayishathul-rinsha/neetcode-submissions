class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        n=len(prices)
        i=0
        while i<n:
            j=0
            while j<i:
                if prices[j]<prices[i]:
                    pr=prices[i]-prices[j]
                    m=max(pr,m)
                j+=1
            i+=1

        return m