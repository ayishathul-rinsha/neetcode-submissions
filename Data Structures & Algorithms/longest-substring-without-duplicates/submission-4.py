class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w=set()
        l=0
        m=0
        n=len(s)
        for r in range(n):
            while s[r] in w:
                w.remove(s[l])
                l+=1
            w.add(s[r])

            m=max(m,r-l+1)
        return m