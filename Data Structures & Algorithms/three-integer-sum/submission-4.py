class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            target=-nums[i]
            l=i+1
            h=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<h:
                if nums[l]+nums[h]==target:
                    res.append([nums[i],nums[l],nums[h]])
                    l+=1
                    while l<h and nums[l]==nums[l-1]:
                        l+=1
                    h-=1
                    while l<h and nums[h]==nums[h+1]:
                        h-=1
                elif nums[l]+nums[h]>target:
                    h-=1
                elif nums[l]+nums[h]<target:
                    l+=1

        return res