from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
       """
       function to sort colors in-place using Dutch National Flag algorithm
       """
       low=0
       mid=0
       high=len(nums)-1
       while mid<=high:
            if nums[mid]==0:
                self.swap(nums,low,mid)
                mid=mid+1
                low=low+1
            elif nums[mid]==1:
                mid=mid+1
            else:
                self.swap(nums,high,mid)
                high=high-1

    def swap(self,nums,i,j):
            """
            function to swap two elements in the list
            """
            k=nums[i]
            nums[i]=nums[j]
            nums[j]=k