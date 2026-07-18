class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        l=0
        s=set(nums)
        i=min(nums) if nums else 0
        n= len(nums)
        for i in s:
            if i-1 not in s:
                no=i
                c=1

                while no+1 in s:
                    no+=1
                    c+=1

                l=max(l,c)
                
            

        return l