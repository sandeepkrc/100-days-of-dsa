from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # steps 1: Create a max heap from the stones list
        # step 2: While there is more than one stone in the heap
        # step 3: Pop the two heaviest stones
        # step 4: If they are not equal, push the difference back into the heap
        # step 5: If there's a stone left, return its weight, otherwise return 0
        # Use a max heap by inverting the stone weights
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Pop the two heaviest stones
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first != second:
                # If they are not equal, push the difference back into the heap
                heapq.heappush(max_heap, -(first - second))
        
        # If there's a stone left, return its weight, otherwise return 0
        #time complexity of this code is O(n log n)
        return -max_heap[0] if max_heap else 0
# Example usage:
stones = [2,7,4,1,8,1]
solution = Solution()
print(solution.lastStoneWeight(stones))  # Output: 1

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use other approach without heap
        # steps 1: While there is more than one stone in the list
        # step 2: Sort the stones in descending order
        # step 3: Pop the two heaviest stones
        # step 4: If they are not equal, append the difference back into the list
        # step 5: If there's a stone left, return its weight, otherwise return

        while len(stones) > 1:
            stones.sort() # time complexicity of sorting is O(n log n)
            first = stones.pop()
            second = stones.pop()
            if first != second:
                stones.append(first - second)

        # time complexity of this code is O(n^2 log n)

        return stones[0] if stones else 0
    
stones = [2,7,4,1,8,1]
solution = Solution()
print(solution.lastStoneWeight(stones))
        