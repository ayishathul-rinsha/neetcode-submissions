class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=len(nums)
        for i in range(r):
            if nums[l]==0:
                nums.append(0)
                nums.pop(l)
            else:
                l+=1
                
        