class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1

            key=tuple(count)

            if key not in d:
                d[key]=[]

            d[key].append(i)

        return list(d.values())