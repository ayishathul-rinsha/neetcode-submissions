class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        s=0
        m=nums[0]
        while l<=h:
            mid=(l+h)//2
            if nums[l]<=nums[mid]:
                s=nums[l]
                m=min(s,m)
                if nums[mid]<=nums[h]:
                    h=mid-1
                else:
                    l=mid+1

                
            elif nums[l]>=nums[mid]:
                s=nums[mid]
                m=min(s,m)
                h=mid-1




        return m      