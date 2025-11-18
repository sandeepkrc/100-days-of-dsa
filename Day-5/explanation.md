# Water Bottles — Explanation

## Problem Statement
You have a certain number of full water bottles, and you can exchange a given number of empty bottles for one full bottle. The goal is to determine the maximum number of water bottles you can drink.

### Problem Details:
- You start with `numBottles` full bottles.
- For every `numExchange` empty bottles, you can exchange them for one full bottle.
- The process continues until you can no longer exchange empty bottles for full ones.

## Approach
### Iterative Approach
- **Idea**: Use a loop to simulate the process of drinking water bottles and exchanging empty bottles for new full ones.
- **Steps**:
  1. Initialize `total_drunk` to `numBottles` (since you drink all the initial bottles).
  2. While the number of full bottles is greater than or equal to `numExchange`:
     - Calculate the number of new bottles you can get: `new_bottles = numBottles // numExchange`.
     - Calculate the remaining empty bottles: `remaining = numBottles % numExchange`.
     - Update `total_drunk` by adding `new_bottles`.
     - Update `numBottles` to the sum of `new_bottles` and `remaining`.
  3. Return `total_drunk`.

### Complexity Analysis:
- **Time Complexity**: O(log(numBottles)), as the number of bottles decreases geometrically with each iteration.
- **Space Complexity**: O(1), as we use only a few variables to store intermediate results.

## Edge Cases
- `numBottles < numExchange`: No exchanges are possible, so the result is simply `numBottles`.
- `numBottles = numExchange`: You can exchange once, so the result is `numBottles + 1`.
- Large values of `numBottles` and `numExchange`: The iterative approach handles this efficiently due to its logarithmic time complexity.

## Example Walkthrough
### Example 1:
- **Input**: `numBottles = 9`, `numExchange = 3`
- **Process**:
  - Start with 9 bottles, drink all → `total_drunk = 9`.
  - Exchange 9 bottles: `new_bottles = 9 // 3 = 3`, `remaining = 9 % 3 = 0`.
  - Update: `total_drunk = 9 + 3 = 12`, `numBottles = 3`.
  - Exchange 3 bottles: `new_bottles = 3 // 3 = 1`, `remaining = 3 % 3 = 0`.
  - Update: `total_drunk = 12 + 1 = 13`, `numBottles = 1`.
  - No more exchanges possible.
- **Output**: `13`.

### Example 2:
- **Input**: `numBottles = 15`, `numExchange = 4`
- **Process**:
  - Start with 15 bottles, drink all → `total_drunk = 15`.
  - Exchange 15 bottles: `new_bottles = 15 // 4 = 3`, `remaining = 15 % 4 = 3`.
  - Update: `total_drunk = 15 + 3 = 18`, `numBottles = 6`.
  - Exchange 6 bottles: `new_bottles = 6 // 4 = 1`, `remaining = 6 % 4 = 2`.
  - Update: `total_drunk = 18 + 1 = 19`, `numBottles = 3`.
  - No more exchanges possible.
- **Output**: `19`.

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!