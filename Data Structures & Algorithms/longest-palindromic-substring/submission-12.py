class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo=''
        m=0
        i=0
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        while i<len(s):
            odd=expand(i,i)
            even=expand(i,i+1)

            if len(odd)>len(lo):
                lo=odd
            if len(even)>len(lo):
                lo=even
            i+=1

        return lo