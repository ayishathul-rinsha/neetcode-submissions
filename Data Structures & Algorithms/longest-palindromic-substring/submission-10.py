class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo=''
        m=0
        i=0
        def expand(l,r):
            nonlocal lo,m
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                if len(s[l:r+1])>m:
                    lo=s[l:r+1]
                    m=len(s[l:r+1])
                l-=1
                r+=1
        while i<len(s):
            expand(i,i)
            expand(i,i+1)

            i+=1

        return lo