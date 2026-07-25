class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=nums[0]
        ms=nums[0]

        for i in range(1,len(nums)):
            num=nums[i]

            cur=max(num, cur+num)

            ms=max(ms, cur)

        return ms