from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
    
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  # [3, 4]
print(sol.searchRange([5,7,7,8,8,10], 6))  # [-1, -1]
print(sol.searchRange([], 0))               # [-1, -1]
        