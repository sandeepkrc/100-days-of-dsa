class Solution:
    def bulbSwitch(self, n):
        count = 0
        i = 1
        while i * i <= n:
            count += 1
            i += 1
        return count
sol = Solution()
print(sol.bulbSwitch(3))  # 1
print(sol.bulbSwitch(0))  # 0
print(sol.bulbSwitch(1))  # 1 