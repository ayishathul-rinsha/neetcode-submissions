class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       d={}
       l=0
       m=0
       mf=0
       n=len(s)
       for r in range(n):
        if s[r] not in d:
            d[s[r]]=0
        d[s[r]]+=1
        mf=max(mf, d[s[r]])
        while ((r-l+1)-mf)>k:
            d[s[l]]-=1
            l+=1
            
        m=max(m,(r-l+1))

       return m