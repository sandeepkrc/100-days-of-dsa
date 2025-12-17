from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        
        return max(pos, neg)
#example

o=Solution()
print(o.maximumCount([1,5,4,5]))


        
        


        