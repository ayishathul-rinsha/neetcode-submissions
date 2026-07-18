class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        m=0
        n=len(s)
        while r<n:
            while s[r] in s[l:r]:
                l+=1
            t=r-l+1
            m=max(m,t)
            r+=1

        return m