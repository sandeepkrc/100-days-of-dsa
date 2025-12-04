from typing import List

class Solution:
    def sortedSquaresBruitefForce(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            output.append(i*i)
        output=sorted(output)
        return output
    
    def sortedSquares(self,nums:List[int]) -> List[int]:

        ans =[0]*len(nums)
        start = 0
        end = len(nums) - 1
        pointer = len(nums) - 1

        while start <= end:
            start_sqrt = nums[start]*nums[start]
            end_sqrt = nums[end]*nums[end]
            if start_sqrt > end_sqrt:
                ans[pointer] = start_sqrt
                start += 1
            else:
                ans[pointer] = end_sqrt
                end -=1
            pointer -= 1
        return ans
        


S=Solution()
print(S.sortedSquaresBruitefForce([-4,-1,0,3,10]))
print(S.sortedSquaresBruitefForce([-7,-3,2,3,11]))


print(S.sortedSquares([-7,-3,2,3,11]))
print(S.sortedSquares([-4,-1,0,3,10]))

