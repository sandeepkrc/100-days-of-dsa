from typing import List

class Solution:

    def bruiteforce(self, numbers: List[int], target: int) -> List[int]:
        answer =[0]*2
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    answer[0] = i + 1
                    answer[1] = j + 1
                    return answer
        return answer
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer =[0]*2
        start = 0
        end = len(numbers)-1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum==target:
                answer[0] = start +1
                answer[1] = end + 1
                return answer
            elif sum < target:
                start = start + 1
            else:
                end = end - 1
        return answer
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # [1,2]
print(sol.twoSum([2,3,4], 6))  # [1,3]
print(sol.twoSum([-1,0], -1))  # [1,2]