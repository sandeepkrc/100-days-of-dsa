from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mamx = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                current_sum += nums[i]
            else:
                mamx = max(mamx, current_sum)
                current_sum = nums[i]
        mamx = max(mamx, current_sum)
        return mamx
sol = Solution()
print(sol.maxAscendingSum([10,20,30,5,10,50]))
print(sol.maxAscendingSum([10,20,30,40,50]))
print(sol.maxAscendingSum([12,17,15,13,10,11,12]))
print(sol.maxAscendingSum([100,10,1]))
        