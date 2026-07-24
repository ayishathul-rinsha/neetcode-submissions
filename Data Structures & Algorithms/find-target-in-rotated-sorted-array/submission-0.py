class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=1001
        t=0
        for i in range(len(nums)):
            if nums[i]<low:
                low=nums[i]
                t=i

        for i in range(t):
            nums.append(nums[i])
            
        nums=nums[t:len(nums)]

        l=0
        h=len(nums)-1
        for i in range(len(nums)):
            mid=(l+h)//2
            if nums[mid]==target:
                return (mid+t)%(len(nums))
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                h=mid-1

        return -1
