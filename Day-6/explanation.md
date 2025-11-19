# Two Sum — Explanation

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

### Problem Details:
- Each input has exactly one solution.
- You may not use the same element twice.
- The solution can be returned in any order.

## Approach
### Hashmap Approach
- **Idea**: Use a hashmap (dictionary) to store the indices of the numbers as you iterate through the array. For each number, calculate the difference between the target and the current number. If the difference exists in the hashmap, return the indices.
- **Steps**:
  1. Initialize an empty hashmap.
  2. Iterate through the array with indices:
     - Calculate the difference: `diff = target - nums[i]`.
     - Check if `diff` exists in the hashmap:
       - If yes, return the indices `[i, hashmap[diff]]`.
       - If no, store the current number and its index in the hashmap.
  3. If no solution is found (though the problem guarantees one), return an empty list.

### Complexity Analysis:
- **Time Complexity**: O(n), as we iterate through the array once and perform constant-time operations for each element.
- **Space Complexity**: O(n), as we store the elements in the hashmap.

## Edge Cases
- `nums` contains negative numbers: The solution works for negative numbers as well.
- `nums` contains duplicate numbers: The solution ensures that the same element is not used twice.
- Small arrays: The solution handles arrays with only two elements correctly.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [2, 7, 11, 15]`, `target = 9`
- **Process**:
  - Initialize `hashmap = {}`.
  - Iterate:
    - `i = 0`, `n = 2`, `diff = 9 - 2 = 7`. `7` is not in `hashmap`. Add `2: 0` to `hashmap`.
    - `i = 1`, `n = 7`, `diff = 9 - 7 = 2`. `2` is in `hashmap`. Return `[1, 0]`.
- **Output**: `[1, 0]`

### Example 2:
- **Input**: `nums = [3, 2, 4]`, `target = 6`
- **Process**:
  - Initialize `hashmap = {}`.
  - Iterate:
    - `i = 0`, `n = 3`, `diff = 6 - 3 = 3`. `3` is not in `hashmap`. Add `3: 0` to `hashmap`.
    - `i = 1`, `n = 2`, `diff = 6 - 2 = 4`. `4` is not in `hashmap`. Add `2: 1` to `hashmap`.
    - `i = 2`, `n = 4`, `diff = 6 - 4 = 2`. `2` is in `hashmap`. Return `[2, 1]`.
- **Output**: `[2, 1]`

### Example 3:
- **Input**: `nums = [3, 3]`, `target = 6`
- **Process**:
  - Initialize `hashmap = {}`.
  - Iterate:
    - `i = 0`, `n = 3`, `diff = 6 - 3 = 3`. `3` is not in `hashmap`. Add `3: 0` to `hashmap`.
    - `i = 1`, `n = 3`, `diff = 6 - 3 = 3`. `3` is in `hashmap`. Return `[1, 0]`.
- **Output**: `[1, 0]`

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!