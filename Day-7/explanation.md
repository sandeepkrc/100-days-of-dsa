# Add to Array-Form of Integer — Explanation

## Problem Statement
Given a non-negative integer represented as an array of digits `num` and an integer `k`, return the array-form of the integer `num + k`.

### Problem Details:
- The array `num` represents the integer in the most significant digit order.
- The integer `k` is added to the number represented by `num`.
- The result should also be returned as an array in the most significant digit order.

## Approach
### Iterative Approach
- **Idea**: Simulate the addition of two numbers digit by digit, starting from the least significant digit (rightmost digit of `num` and `k`). Use a carry to handle overflow.
- **Steps**:
  1. Initialize an empty list `result` to store the digits of the sum.
  2. Use a pointer to traverse `num` from the least significant digit (rightmost digit).
  3. While there are digits left in `num` or `k` or there is a carry:
     - Extract the current digit from `num` (if the pointer is valid) and from `k`.
     - Compute the sum of the digits and the carry.
     - Update the carry for the next iteration.
     - Append the least significant digit of the sum to `result`.
     - Move the pointer left and reduce `k` by dividing it by 10.
  4. Reverse the `result` list to get the most significant digit order.
  5. Return the `result`.

### Complexity Analysis:
- **Time Complexity**: O(max(n, log k)), where `n` is the length of `num` and `log k` is the number of digits in `k`. This is because we process each digit of `num` and `k` at most once.
- **Space Complexity**: O(max(n, log k)), as we store the result in a list.

## Edge Cases
- `num` is empty: The result is simply the digits of `k`.
- `k` is 0: The result is the same as `num`.
- Large values of `k`: The algorithm handles large `k` efficiently by processing its digits one by one.
- Carry propagation: Ensure that the carry is correctly handled when adding the last digits.

## Example Walkthrough
### Example 1:
- **Input**: `num = [1, 2, 0, 0]`, `k = 34`
- **Process**:
  - Initialize `result = []`, `carry = 0`, `pointer = 3`.
  - Iteration 1: `digit_num = 0`, `digit_k = 4`, `total = 0 + 4 + 0 = 4`. Append `4` to `result`. Update `carry = 0`, `pointer = 2`, `k = 3`.
  - Iteration 2: `digit_num = 0`, `digit_k = 3`, `total = 0 + 3 + 0 = 3`. Append `3` to `result`. Update `carry = 0`, `pointer = 1`, `k = 0`.
  - Iteration 3: `digit_num = 2`, `digit_k = 0`, `total = 2 + 0 + 0 = 2`. Append `2` to `result`. Update `carry = 0`, `pointer = 0`, `k = 0`.
  - Iteration 4: `digit_num = 1`, `digit_k = 0`, `total = 1 + 0 + 0 = 1`. Append `1` to `result`. Update `carry = 0`, `pointer = -1`, `k = 0`.
  - Reverse `result = [4, 3, 2, 1]`.
- **Output**: `[1, 2, 3, 4]`

### Example 2:
- **Input**: `num = [2, 7, 4]`, `k = 181`
- **Process**:
  - Similar steps as above.
- **Output**: `[4, 5, 5]`

### Example 3:
- **Input**: `num = [2, 1, 5]`, `k = 806`
- **Process**:
  - Similar steps as above.
- **Output**: `[1, 0, 2, 1]`

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!