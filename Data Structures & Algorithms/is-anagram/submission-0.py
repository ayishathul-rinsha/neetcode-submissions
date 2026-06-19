class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        e={}
        s="".join(sorted(s))
        t="".join(sorted(t))
        for i in s:
            if i not in d:
                d[i]=s.count(i)
        for i in t:
            if i not in e:
                e[i]=t.count(i)

        if d==e:
            return True
        else:
            return False

        