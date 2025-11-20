from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        pointer= len(num) - 1
        while pointer >= 0 or k > 0 or carry > 0:
            if pointer >= 0:
                digit_num =num[pointer]
            else:
                digit_num = 0
            digit_k = k % 10 # getting the last digit of k
            total = digit_num + digit_k + carry 
            carry = total // 10. # calculating carry for next iteration
            result.append(total % 10)
            pointer -= 1
            k //= 10. # removing the last digit of k
        return result[::-1]
    
    def brutforce(self, num: List[int], k: int) -> List[int]:
        # Convert the array-form number to an integer
        num_as_int = 0
        for digit in num:
            num_as_int = num_as_int * 10 + digit
        
        # Add k to the integer
        total = num_as_int + k
        
        # Convert the result back to array-form
        result = []
        if total == 0:
            return [0]
        while total > 0:
            result.append(total % 10)
            total //= 10
        
        return result[::-1]

sol = Solution()
print(sol.addToArrayForm([1,2,0,0],34))  # [1,2,3,4]
print(sol.addToArrayForm([2,7,4],181))  # [4,5,5]
print(sol.addToArrayForm([2,1,5],806))  # [1,0,2,1]
      