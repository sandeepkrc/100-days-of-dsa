# Remove Element — Explanation

## Problem Statement
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The relative order of the elements may be changed. Return the number of elements in `nums` which are not equal to `val`.

### Problem Details:
- The function must modify the input array in-place.
- The result should be the count of elements not equal to `val`.
- The first `k` elements of the array should contain the elements not equal to `val`.

## Approach
### Two-Pointer Technique
- **Idea**: Use a pointer `k` to track the position of the next non-`val` element. Iterate through the array, and whenever an element is not equal to `val`, move it to the position pointed to by `k`.
- **Steps**:
  1. Initialize `k = 0` to track the position of the next non-`val` element.
  2. Iterate through the array using a loop:
     - If the current element is not equal to `val`, assign it to `nums[k]` and increment `k`.
  3. Return `k` as the count of elements not equal to `val`.

### Complexity Analysis:
- **Time Complexity**: O(n), where `n` is the length of the array. We iterate through the array once.
- **Space Complexity**: O(1), as we modify the array in-place and use only a few variables.

## Edge Cases
- `nums` is empty: The result is `0`.
- `nums` contains only `val`: The result is `0`.
- `nums` contains no occurrences of `val`: The result is the length of `nums`.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [3, 2, 2, 3]`, `val = 3`
- **Process**:
  - Initialize `k = 0`.
  - Iterate:
    - `i = 0`, `nums[i] = 3`: Skip as it equals `val`.
    - `i = 1`, `nums[i] = 2`: Assign `nums[k] = nums[i]`, increment `k` to `1`.
    - `i = 2`, `nums[i] = 2`: Assign `nums[k] = nums[i]`, increment `k` to `2`.
    - `i = 3`, `nums[i] = 3`: Skip as it equals `val`.
  - Final array: `nums = [2, 2, _, _]` (where `_` represents irrelevant values).
- **Output**: `2`

### Example 2:
- **Input**: `nums = [0, 1, 2, 2, 3, 0, 4, 2]`, `val = 2`
- **Process**:
  - Initialize `k = 0`.
  - Iterate:
    - `i = 0`, `nums[i] = 0`: Assign `nums[k] = nums[i]`, increment `k` to `1`.
    - `i = 1`, `nums[i] = 1`: Assign `nums[k] = nums[i]`, increment `k` to `2`.
    - `i = 2`, `nums[i] = 2`: Skip as it equals `val`.
    - `i = 3`, `nums[i] = 2`: Skip as it equals `val`.
    - `i = 4`, `nums[i] = 3`: Assign `nums[k] = nums[i]`, increment `k` to `3`.
    - `i = 5`, `nums[i] = 0`: Assign `nums[k] = nums[i]`, increment `k` to `4`.
    - `i = 6`, `nums[i] = 4`: Assign `nums[k] = nums[i]`, increment `k` to `5`.
    - `i = 7`, `nums[i] = 2`: Skip as it equals `val`.
  - Final array: `nums = [0, 1, 3, 0, 4, _, _, _]`.
- **Output**: `5`

### Example 3:
- **Input**: `nums = [1]`, `val = 1`
- **Process**:
  - Initialize `k = 0`.
  - Iterate:
    - `i = 0`, `nums[i] = 1`: Skip as it equals `val`.
  - Final array: `nums = [_]`.
- **Output**: `0`

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!