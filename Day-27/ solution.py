from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Ensure mid is even for comparison
            if mid % 2 == 1:
                mid -= 1
            
            # Check if the pair is valid
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        
        return nums[left]
    
# Example usage:
s=Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Output: 2
print(s.singleNonDuplicate([3,3,7,7,10,11,11]))  # Output: 10
