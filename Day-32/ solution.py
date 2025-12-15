from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings for comparison
        str_nums = list(map(str, nums))
        
        # Custom comparator function
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort the numbers based on the custom comparator
        from functools import cmp_to_key
        str_nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        largest_num = ''.join(str_nums)
        
        # Handle the case where the result is all zeros
        return '0' if largest_num[0] == '0' else largest_num
# Example usage:
solution = Solution()
print(solution.largestNumber([10, 2]))        # Output: "210"
print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"
print(solution.largestNumber([0, 0]))         # Output: "0"



        
