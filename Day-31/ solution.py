from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Count occurrences of numbers less than, equal to, and greater than target

        less_count = 0
        equal_count = 0
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                equal_count += 1
        ans=[]
        while equal_count > 0:
            ans.append(less_count)
            less_count += 1
            equal_count -= 1
        return ans
    
# Example usage:
solution = Solution()
print(solution.targetIndices([1,2,5,2,3], 2))  # Output: [1, 2]


