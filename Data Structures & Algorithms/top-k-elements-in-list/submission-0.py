class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        n=len(nums)
        count=[[] for i in range(n+1)]
        for i in nums:
            if i not in d:
                d[i]=0

            d[i]+=1

        for num,f in d.items():
            count[f].append(num)

        r=[]

        for i in range((len(count))-1,0,-1): 
            for j in count[i]:
                r.append(j)

                if len(r)==k:
                    return r