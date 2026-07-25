class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cx=nums[0]
        mp=nums[0]
        cn=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            
            c1=cx*num
            c2=cn*num

            cx=max(num,c1,c2)
            cn=min(num,c1,c2)

            mp=max(mp,cx)

        return mp