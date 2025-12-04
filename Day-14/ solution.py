class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0]*length

        # Calculate left products
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        # Calculate right products and final result
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(sol.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
