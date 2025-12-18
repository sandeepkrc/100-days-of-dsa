from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move backwards
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        
        # If all digits were 9, we need to add a new digit at the front
        return [1] + [0] * n
    
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # [1, 2, 4]
print(sol.plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
print(sol.plusOne([9]))  # [1, 0]
        




        





        