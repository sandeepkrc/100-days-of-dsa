# Squares of a Sorted Array — Explanation

## Problem Statement
Given an integer array `nums` sorted in **non-decreasing order**, return an array of the squares of each number sorted in **non-decreasing order**.

### Problem Details:
- The input array `nums` may contain negative numbers.
- Squaring a negative number makes it positive, so the order of the squared values may change.
- The output array must be sorted in non-decreasing order.

## Approach
### Solution 1: Brute Force
- **Idea**: Square each element in the array and then sort the resulting array.
- **Steps**:
  1. Initialize an empty list `output`.
  2. Iterate through the array, square each element, and append it to `output`.
  3. Sort the `output` list.
  4. Return the sorted list.
- **Complexity**:
  - Time Complexity: O(n log n), where `n` is the length of the array. This is due to the sorting step.
  - Space Complexity: O(n), as we use an additional list to store the squared values.

### Solution 2: Two-Pointer Technique (Optimal Solution)
- **Idea**: Use two pointers, one at the start and one at the end of the array. Compare the squares of the elements at these pointers and place the larger square at the end of the result array.
- **Steps**:
  1. Initialize two pointers: `start` at the beginning of the array and `end` at the end of the array.
  2. Initialize a `pointer` at the end of the result array.
  3. While `start <= end`:
     - Compute the square of the element at `start` and `end`.
     - Place the larger square at the position indicated by `pointer` in the result array.
     - Move the `start` pointer forward if its square was larger, otherwise move the `end` pointer backward.
     - Decrement the `pointer`.
  4. Return the result array.
- **Complexity**:
  - Time Complexity: O(n), as we iterate through the array once.
  - Space Complexity: O(n), as we use an additional array to store the result.

### Comparison
- The brute force solution is simpler but less efficient due to the sorting step.
- The two-pointer technique is optimal and avoids the need for sorting.

## Edge Cases
- `nums` is empty: The result is an empty array.
- `nums` contains all positive numbers: The result is the squares of the numbers in the same order.
- `nums` contains all negative numbers: The result is the squares of the numbers in reverse order.
- `nums` contains zeros: The result includes zeros, which do not affect the order.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [-4, -1, 0, 3, 10]`
- **Process (Two-Pointer Technique)**:
  - Initialize `start = 0`, `end = 4`, `pointer = 4`, `ans = [0, 0, 0, 0, 0]`.
  - Iteration 1: Compare `(-4)^2 = 16` and `(10)^2 = 100`. Place `100` at `ans[4]`. Update `end = 3`, `pointer = 3`.
  - Iteration 2: Compare `(-4)^2 = 16` and `(3)^2 = 9`. Place `16` at `ans[3]`. Update `start = 1`, `pointer = 2`.
  - Iteration 3: Compare `(-1)^2 = 1` and `(3)^2 = 9`. Place `9` at `ans[2]`. Update `end = 2`, `pointer = 1`.
  - Iteration 4: Compare `(-1)^2 = 1` and `(0)^2 = 0`. Place `1` at `ans[1]`. Update `start = 2`, `pointer = 0`.
  - Iteration 5: Place `0` at `ans[0]`. Update `start = 3`, `pointer = -1`.
  - Final result: `ans = [0, 1, 9, 16, 100]`.
- **Output**: `[0, 1, 9, 16, 100]`

### Example 2:
- **Input**: `nums = [-7, -3, 2, 3, 11]`
- **Process (Two-Pointer Technique)**:
  - Similar steps as above.
- **Output**: `[4, 9, 9, 49, 121]`

---

This explanation provides a clear understanding of the problem, the approaches used to solve it, and the reasoning behind each step. Happy coding!