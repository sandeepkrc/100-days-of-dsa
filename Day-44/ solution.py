from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Steps
        # 1. Sort the list of people by their weights.
        # 2. Use two pointers: one starting at the lightest person and the other at the heaviest.
        # 3. If the sum of weights of both pointers is less than or equal to the limit, move both pointers inward (indicating both people can share a boat).
        # 4. If the sum exceeds the limit, move only the pointer at the heaviest person inward (indicating only the heaviest person gets a boat).
        # 5. Increment the boat count each time a boat is allocated.
        # 6. Continue until all people are allocated boats.
    
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
            
        return boats
    

        