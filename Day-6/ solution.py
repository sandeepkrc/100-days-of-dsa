from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[n]=i


sol = Solution()
print(sol.twoSum([2,7,11,15],9))  # [1,0]
print(sol.twoSum([3,2,4],6))  # [2,1]
print(sol.twoSum([3,3],6))  # [1,0]

