from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which side is properly sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:  # Target in the left side
                    right = mid - 1
                else:  # Target in the right side
                    left = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:  # Target in the right side
                    left = mid + 1
                else:  # Target in the left side
                    right = mid - 1
        
        return -1
# Example usage:
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
        