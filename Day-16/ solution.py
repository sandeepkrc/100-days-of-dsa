class Solution:
    def dominantIndex(self, nums):
        maxm=-1
        second=-1
        maxIdx=0
        for i in range(len(nums)):
            if maxm<nums[i]:
                second =maxm
                maxm =nums[i]
                maxIdx=i
            elif second<nums[i]:
                second =nums[i]
        if second*2<=maxm:
            return maxIdx
        else:
            return -1

s=Solution()
print(s.dominantIndex([3,6,1,0]))

