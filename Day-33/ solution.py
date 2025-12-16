from typing import List, Tuple

class Solution:
    

    def maximumCount(self, nums: List[int]) -> int:
        negative_count = sum(1 for x in nums if x < 0)
        positive_count = sum(1 for x in nums if x > 0)
        return max(negative_count, positive_count)

    def minimumCount(self, nums: List[int]) -> int:
        negative_count = sum(1 for x in nums if x < 0)
        positive_count = sum(1 for x in nums if x > 0)
        return min(negative_count, positive_count)

#example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, -2, 0, 1, 2]
    print("Maximum Count:", solution.maximumCount(nums))  # Output: 3
    print("Minimum Count:", solution.minimumCount(nums))  # Output: 2
    nums = [-2,-1,-1,1,2,3]
    print("Maximum Count:", solution.maximumCount(nums))  # Output: 4
    print("Minimum Count:", solution.minimumCount(nums))  # Output: 2