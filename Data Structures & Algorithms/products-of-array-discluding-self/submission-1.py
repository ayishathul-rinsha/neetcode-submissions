class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n
        p=[1]*n
        s=[1]*n
        i=0
        while i<n:
            j=0
            while j<i:
                p[i]*=nums[j]
                j+=1
            i+=1

        i=0
        while i<n:
            j=i+1
            while j<n:
                s[i]*=nums[j]
                j+=1
            i+=1

        i=0
        while i<n:
            output[i]=p[i]*s[i]
            i+=1

        return output