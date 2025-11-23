from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        # actual sum of elements in the array when there is one missing number
        actual_sum = sum(nums)
        return expected_sum - actual_sum
 
    # brute force solution
    def missingNumberBruteForce(self, nums: List[int]) -> int:
        n = len(nums)
        for number in range(n + 1):
            if number not in nums:
                return number
        return -1  # This line should never be reached
    
sol = Solution()
print(sol.missingNumber([3, 0, 1]))  # 2
print(sol.missingNumber([0, 1]))     # 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # 8
print(sol.missingNumber([0]))        # 1
# Testing the brute force solution
print(sol.missingNumberBruteForce([3, 0, 1]))  # 2
print(sol.missingNumberBruteForce([0, 1]))     # 2
print(sol.missingNumberBruteForce([9,6,4,2,3,5,7,0,1]))  # 8
print(sol.missingNumberBruteForce([0]))        # 1