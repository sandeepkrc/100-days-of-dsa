# Binary Search — Explanation

## Problem Statement
Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists in the array. If `target` does not exist, return `-1`.

### Problem Details:
- The array `nums` is sorted in ascending order.
- The solution must run in O(log n) time.
- If the `target` exists in the array, return its index.
- If the `target` does not exist, return `-1`.

## Approach
### Binary Search
- **Idea**: Use the binary search algorithm to efficiently find the `target` in the sorted array.
- **Steps**:
  1. Initialize two pointers: `start` at the beginning of the array and `end` at the end of the array.
  2. While `start` is less than or equal to `end`:
     - Calculate the middle index: `mid = (start + end) // 2`.
     - If `nums[mid]` equals `target`, return `mid`.
     - If `target` is greater than `nums[mid]`, move the `start` pointer to `mid + 1`.
     - If `target` is less than `nums[mid]`, move the `end` pointer to `mid - 1`.
  3. If the loop ends without finding the `target`, return `-1`.

### Complexity
- **Time Complexity**: O(log n), as we repeatedly divide the search space in half.
- **Space Complexity**: O(1), as we use only a constant amount of extra space.

## Edge Cases
- `nums` is empty: Return `-1`.
- `target` is smaller than all elements in `nums`: Return `-1`.
- `target` is larger than all elements in `nums`: Return `-1`.
- `target` is not in `nums`: Return `-1`.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`
- **Process**:
  - `start = 0`, `end = 5`, `mid = 2`, `nums[mid] = 3`.
  - `target > nums[mid]`, so `start = mid + 1 = 3`.
  - `start = 3`, `end = 5`, `mid = 4`, `nums[mid] = 9`.
  - `nums[mid] == target`, return `4`.
- **Output**: `4`

### Example 2:
- **Input**: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2`
- **Process**:
  - `start = 0`, `end = 5`, `mid = 2`, `nums[mid] = 3`.
  - `target < nums[mid]`, so `end = mid - 1 = 1`.
  - `start = 0`, `end = 1`, `mid = 0`, `nums[mid] = -1`.
  - `target > nums[mid]`, so `start = mid + 1 = 1`.
  - `start = 1`, `end = 1`, `mid = 1`, `nums[mid] = 0`.
  - `target > nums[mid]`, so `start = mid + 1 = 2`.
  - `start > end`, return `-1`.
- **Output**: `-1`

### Example 3:
- **Input**: `nums = []`, `target = 1`
- **Process**:
  - `start = 0`, `end = -1`, `start > end`, return `-1`.
- **Output**: `-1`

---

This explanation provides a clear understanding of the problem, the binary search approach, and the reasoning behind each step. Happy coding!
