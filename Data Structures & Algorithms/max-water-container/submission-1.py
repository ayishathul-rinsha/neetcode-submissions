class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        m=0
        h=len(heights)-1
        while l<h:
            ar=(h-l)*min(heights[h],heights[l])
            m=max(ar,m)
            if heights[h]<=heights[l]:
                h-=1
            else:
                l+=1

        return m