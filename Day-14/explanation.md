# Product of Array Except Self — Explanation

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

### Problem Details:
- Solve the problem **without using division**.
- The solution must run in O(n) time.
- The input array may contain positive, negative, and zero values.

## Approach
### Left and Right Product Technique
- **Idea**: Use two passes to calculate the product of all elements except the current one:
  1. In the first pass, calculate the product of all elements to the left of each index.
  2. In the second pass, calculate the product of all elements to the right of each index and multiply it with the left product.
- **Steps**:
  1. Initialize an array `answer` where `answer[i]` will store the product of all elements except `nums[i]`.
  2. Compute the left products:
     - Set `answer[0] = 1` (no elements to the left of the first element).
     - For each index `i` from 1 to `n-1`, set `answer[i] = nums[i-1] * answer[i-1]`.
  3. Compute the right products and update `answer`:
     - Initialize `R = 1` (no elements to the right of the last element).
     - Traverse the array in reverse, updating `answer[i] = answer[i] * R` and `R = R * nums[i]`.
  4. Return `answer`.

### Complexity
- **Time Complexity**: O(n), as we traverse the array twice (once for left products and once for right products).
- **Space Complexity**: O(1) (excluding the output array), as we use only a constant amount of extra space.

## Edge Cases
- `nums` contains zeros: The result for indices with zeros will be zero unless the zero is the only zero in the array.
- `nums` contains one element: The result is an empty array or undefined behavior.
- `nums` contains negative numbers: The solution handles negative numbers correctly.

## Example Walkthrough
### Example 1:
- **Input**: `nums = [1, 2, 3, 4]`
- **Process**:
  - Left products:
    - `answer = [1, 1, 2, 6]` (calculated as `[1, 1*1, 1*2, 1*2*3]`).
  - Right products:
    - Multiply by right products in reverse: `answer = [24, 12, 8, 6]`.
- **Output**: `[24, 12, 8, 6]`

---

This explanation provides a clear understanding of the problem, the left and right product technique, and the reasoning behind each step. Happy coding!