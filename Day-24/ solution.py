from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif nums[0]<nums[len(nums)-1]:
            return nums[0]
        else:  
            pass
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>nums[mid+1] and mid!=len(nums)-1:#
                return nums[mid+1]
            elif nums[mid-1]>nums[mid] and mid!=0:# right side is sorted, go to left side
                return nums[mid]
            elif nums[mid]>nums[0]:# left side is sorted, go to right side
                start=mid+1
            else:
                end=mid-1
sol = Solution()
print(sol.findMin([3,4,5,1,2]))  # 1
print(sol.findMin([4,5,6,7,0,1,2]))  # 0
print(sol.findMin([11,13,15,17]))  # 11
    