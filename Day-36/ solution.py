from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total_salary = sum(salary)
        adjusted_total = total_salary - min_salary - max_salary
        adjusted_count = len(salary) - 2
        return adjusted_total / adjusted_count
    
sol = Solution()
print(sol.average([4000,3000,1000,2000]))  # 2500.0
print(sol.average([1000,2000,3000]))