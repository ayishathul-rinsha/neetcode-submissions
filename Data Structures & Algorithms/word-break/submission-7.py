class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st=set(wordDict)
        d={}
        for i in range(len(s)+1):
            d[i]=False
        d[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if d[j]==True and s[j:i] in st:
                    d[i]=True
                    break
        return d[len(s)]