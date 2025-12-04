from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the position of the next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))  # Output: 2
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5
print(sol.removeElement([1], 1))  # Output: 0
        