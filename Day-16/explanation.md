# Largest Number At Least Twice of Others — Explanation

## Problem Statement
You are given an integer array `nums` where the largest integer is at least twice as large as every other number in the array. Return the index of the largest number, or return `-1` if no such number exists.

### Problem Details:
- The largest number in the array must be at least twice as large as every other number.
- If this condition is satisfied, return the index of the largest number.
- Otherwise, return `-1`.

## Approach
### Key Insight
To solve this problem, we need to:
1. Identify the largest number in the array and its index.
2. Track the second largest number in the array.
3. Check if the largest number is at least twice as large as the second largest number.

### Steps
1. Initialize variables:
   - `maxm` to store the largest number (initially set to `-1`).
   - `second` to store the second largest number (initially set to `-1`).
   - `maxIdx` to store the index of the largest number.
2. Iterate through the array:
   - If the current number is greater than `maxm`, update `second` to `maxm`, update `maxm` to the current number, and update `maxIdx` to the current index.
   - Otherwise, if the current number is greater than `second`, update `second` to the current number.
3. After the loop, check if `second * 2 <= maxm`:
   - If true, return `maxIdx`.
   - Otherwise, return `-1`.

### Complexity
- **Time Complexity**: O(n), as we iterate through the array once.
- **Space Complexity**: O(1), as we use only a constant amount of extra space.

## Edge Cases
- Array contains only one element: The result is the index `0`.
- All elements are the same: The result is the index of the largest number.
- The largest number is not at least twice as large as another number: The result is `-1`.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [3, 6, 1, 0]`
- **Process**:
  - Largest number: `6` (index `1`).
  - Second largest number: `3`.
  - Check: `3 * 2 <= 6` → True.
- **Output**: `1`

### Example 2:
- **Input**: `nums = [1, 2, 3, 4]`
- **Process**:
  - Largest number: `4` (index `3`).
  - Second largest number: `3`.
  - Check: `3 * 2 <= 4` → False.
- **Output**: `-1`

### Example 3:
- **Input**: `nums = [1]`
- **Process**:
  - Largest number: `1` (index `0`).
  - Second largest number: `-1` (no other elements).
  - Check: `-1 * 2 <= 1` → True.
- **Output**: `0`

---

This explanation provides a clear understanding of the problem, the solution approach, and the reasoning behind each step. Happy coding!
