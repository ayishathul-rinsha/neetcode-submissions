class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        n=len(prices)
        i=0
        l=prices[0]
        while i<n:
            if prices[i]<l:
                l=prices[i]
            else:
                pr=prices[i]-l
                m=max(m,pr)
            i+=1

        return m