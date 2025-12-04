# Maximum Product Subarray — Explanation

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array (containing at least one number) that has the largest product, and return the product.

### Problem Details:
- The array may contain positive, negative, and zero values.
- The subarray must be contiguous.

## Approach
### Dynamic Programming with Two Variables
- **Idea**: Use two variables to keep track of the maximum and minimum product at each index. This is necessary because a negative number can turn a small product into a large one and vice versa.
- **Steps**:
  1. Initialize `max_product`, `min_product`, and `result` to the first element of the array.
  2. Iterate through the array starting from the second element:
     - If the current number is negative, swap `max_product` and `min_product`.
     - Update `max_product` to be the maximum of the current number and the product of `max_product` and the current number.
     - Update `min_product` to be the minimum of the current number and the product of `min_product` and the current number.
     - Update `result` to be the maximum of `result` and `max_product`.
  3. Return `result`.

### Complexity Analysis:
- **Time Complexity**: O(n), where `n` is the length of the array. We iterate through the array once.
- **Space Complexity**: O(1), as we use only a few variables to store intermediate results.

## Edge Cases
- Single-element array: The result is the single element.
- Array contains zeros: Zeros reset the product, so the subarray must start after the zero.
- Array contains all negative numbers: The result is the product of the entire array if the count of negative numbers is even; otherwise, it excludes one negative number.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [2, 3, -2, 4]`
- **Process**:
  - Initialize `max_product = 2`, `min_product = 2`, `result = 2`.
  - Iterate:
    - `i = 1`, `nums[i] = 3`:
      - `max_product = max(3, 2 * 3) = 6`
      - `min_product = min(3, 2 * 3) = 3`
      - `result = max(2, 6) = 6`
    - `i = 2`, `nums[i] = -2`:
      - Swap `max_product` and `min_product`.
      - `max_product = max(-2, 3 * -2) = -2`
      - `min_product = min(-2, 6 * -2) = -12`
      - `result = max(6, -2) = 6`
    - `i = 3`, `nums[i] = 4`:
      - `max_product = max(4, -2 * 4) = 4`
      - `min_product = min(4, -12 * 4) = -48`
      - `result = max(6, 4) = 6`
- **Output**: `6`

### Example 2:
- **Input**: `nums = [-2, 0, -1]`
- **Process**:
  - Initialize `max_product = -2`, `min_product = -2`, `result = -2`.
  - Iterate:
    - `i = 1`, `nums[i] = 0`:
      - `max_product = max(0, -2 * 0) = 0`
      - `min_product = min(0, -2 * 0) = 0`
      - `result = max(-2, 0) = 0`
    - `i = 2`, `nums[i] = -1`:
      - `max_product = max(-1, 0 * -1) = 0`
      - `min_product = min(-1, 0 * -1) = -1`
      - `result = max(0, 0) = 0`
- **Output**: `0`

### Example 3:
- **Input**: `nums = [-2, 3, -4]`
- **Process**:
  - Initialize `max_product = -2`, `min_product = -2`, `result = -2`.
  - Iterate:
    - `i = 1`, `nums[i] = 3`:
      - `max_product = max(3, -2 * 3) = 3`
      - `min_product = min(3, -2 * 3) = -6`
      - `result = max(-2, 3) = 3`
    - `i = 2`, `nums[i] = -4`:
      - Swap `max_product` and `min_product`.
      - `max_product = max(-4, -6 * -4) = 24`
      - `min_product = min(-4, 3 * -4) = -12`
      - `result = max(3, 24) = 24`
- **Output**: `24`

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!