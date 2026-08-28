class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo=''
        m=0
        i=0
        while i<len(s):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                if len(s[l:r+1])>m:
                    lo=s[l:r+1]
                    m=len(s[l:r+1])
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1])>m:
                    lo=s[l:r+1]
                    m=len(s[l:r+1])
                l-=1
                r+=1

            i+=1

        return lo