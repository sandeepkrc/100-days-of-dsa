from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        out={}
        for ele in arr:
            if ele not in out:
                out[ele] = 1
            else:
                out[ele] += 1
        ans = -1
        for key, value in out.items():
            if key == value:
                ans = max(ans, key)
        return ans

s=Solution()
print(s.findLucky([2,2,3,4]))
print(s.findLucky([1,2,2,3,3,3]))
print(s.findLucky([5]))
print(s.findLucky([7,7,7,7,7,7,7]))
        