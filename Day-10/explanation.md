# Missing Number — Explanation

## Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### Problem Details:
- The array contains `n` distinct numbers, meaning one number in the range `[0, n]` is missing.
- The task is to find and return the missing number efficiently.

## Approach
### Solution 1: Sum Formula (Efficient Approach)
- **Idea**: The sum of the first `n` natural numbers is given by the formula `n * (n + 1) / 2`. By subtracting the sum of the elements in the array from this expected sum, we can find the missing number.
- **Steps**:
  1. Calculate the expected sum of numbers from `0` to `n` using the formula: `expected_sum = n * (n + 1) // 2`.
  2. Calculate the actual sum of the elements in the array: `actual_sum = sum(nums)`.
  3. The missing number is `expected_sum - actual_sum`.
- **Complexity**:
  - Time Complexity: O(n), as we calculate the sum of the array in linear time.
  - Space Complexity: O(1), as we use only a few variables.

### Solution 2: Brute Force
- **Idea**: Check each number in the range `[0, n]` to see if it is present in the array. If a number is not found, it is the missing number.
- **Steps**:
  1. Iterate through all numbers from `0` to `n`.
  2. For each number, check if it is in the array.
  3. Return the first number that is not found.
- **Complexity**:
  - Time Complexity: O(n^2), as we perform a membership check for each number in the range.
  - Space Complexity: O(1), as we use no additional data structures.

### Comparison
- The sum formula approach is much more efficient than the brute force approach, especially for large arrays.
- The brute force approach is simple but impractical for large inputs due to its quadratic time complexity.

## Edge Cases
- `nums` is empty: The missing number is `0`.
- `nums` contains all numbers except the largest one: The missing number is `n`.
- `nums` contains all numbers except `0`: The missing number is `0`.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [3, 0, 1]`
- **Process**:
  - `n = 3`
  - `expected_sum = 3 * (3 + 1) / 2 = 6`
  - `actual_sum = 3 + 0 + 1 = 4`
  - `missing_number = expected_sum - actual_sum = 6 - 4 = 2`
- **Output**: `2`

### Example 2:
- **Input**: `nums = [0, 1]`
- **Process**:
  - `n = 2`
  - `expected_sum = 2 * (2 + 1) / 2 = 3`
  - `actual_sum = 0 + 1 = 1`
  - `missing_number = expected_sum - actual_sum = 3 - 1 = 2`
- **Output**: `2`

### Example 3:
- **Input**: `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`
- **Process**:
  - `n = 9`
  - `expected_sum = 9 * (9 + 1) / 2 = 45`
  - `actual_sum = 9 + 6 + 4 + 2 + 3 + 5 + 7 + 0 + 1 = 37`
  - `missing_number = expected_sum - actual_sum = 45 - 37 = 8`
- **Output**: `8`

---

This explanation provides a clear understanding of the problem, the approaches used to solve it, and the reasoning behind each step. Happy coding!