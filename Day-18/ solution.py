from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    def increasingTripletBruteForce(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False
    
    
sol = Solution()
print(sol.increasingTriplet([1, 2, 3, 4, 5]))  # True
print(sol.increasingTriplet([5, 4, 3, 2, 1]))  # False
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
        