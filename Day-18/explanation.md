# Increasing Triplet Subsequence — Explanation

## Problem Statement
Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that:
- `i < j < k`, and
- `nums[i] < nums[j] < nums[k]`.

If no such indices exist, return `false`.

### Problem Details:
- The goal is to determine if there exists an increasing subsequence of length 3 in the array.
- The solution must run in O(n) time and use O(1) space.

## Approach
### Greedy Technique
- **Idea**: Use two variables, `first` and `second`, to track the smallest and second smallest numbers in the array. If we find a number greater than `second`, we know an increasing triplet exists.
- **Steps**:
  1. Initialize `first` and `second` to infinity.
  2. Iterate through the array:
     - If the current number is smaller than or equal to `first`, update `first`.
     - Else if the current number is smaller than or equal to `second`, update `second`.
     - Else, return `True` (a number greater than `second` is found).
  3. If the loop completes without finding such a number, return `False`.

### Complexity
- **Time Complexity**: O(n), as we traverse the array once.
- **Space Complexity**: O(1), as we use only two variables.

## Edge Cases
- Array length less than 3: Return `False` (not enough elements for a triplet).
- All elements are the same: Return `False` (no increasing subsequence).
- Array contains negative numbers: The solution handles negative numbers correctly.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [1, 2, 3, 4, 5]`
- **Process**:
  - `first = 1`, `second = 2`, `3 > second` → Return `True`.
- **Output**: `True`

### Example 2:
- **Input**: `nums = [5, 4, 3, 2, 1]`
- **Process**:
  - `first = 5`, `second = inf`, no number greater than `second` → Return `False`.
- **Output**: `False`

### Example 3:
- **Input**: `nums = [2, 1, 5, 0, 4, 6]`
- **Process**:
  - `first = 1`, `second = 4`, `6 > second` → Return `True`.
- **Output**: `True`

---

This explanation provides a clear understanding of the problem, the greedy approach, and the reasoning behind each step. Happy coding!
