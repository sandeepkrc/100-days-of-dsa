from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            ele=nums[i]
            ele=abs(ele)

            if nums[ele]>0:
                nums[ele]=-nums[ele]
            else:
                ans= ele
                break
        
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        
        return ans
        