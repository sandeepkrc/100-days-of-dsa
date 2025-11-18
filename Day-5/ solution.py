class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        total_drunk = numBottles
        
        while numBottles >= numExchange:
            new_bottles = numBottles/numExchange
            remaining = numBottles%numExchange
            total_drunk = total_drunk + new_bottles
            numBottles = remaining + new_bottles
        return total_drunk


sol = Solution()
print(sol.numWaterBottles(9, 3))  # 13
print(sol.numWaterBottles(15, 4))  # 19
print(sol.numWaterBottles(5, 5))  # 6

    





        
