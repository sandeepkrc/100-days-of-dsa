# Tribonacci Number — Explanation

## Problem Statement
The Tribonacci sequence is a generalization of the Fibonacci sequence where each term is the sum of the three preceding ones. The sequence is defined as follows:

- T(0) = 0
- T(1) = 1
- T(2) = 1
- T(n) = T(n-1) + T(n-2) + T(n-3), for n >= 3

Given an integer `n`, calculate `T(n)`.

## Approach
### Iterative Approach
- **Idea**: Use an iterative approach to calculate the Tribonacci numbers, storing only the last three numbers to save space.
- **Steps**:
  1. If `n == 0`, return 0.
  2. If `n == 1` or `n == 2`, return 1.
  3. Initialize three variables: `t0 = 0`, `t1 = 1`, `t2 = 1`.
  4. Use a loop from 3 to `n`, updating the variables to calculate the next Tribonacci number.
  5. Return the last calculated Tribonacci number.
- **Complexity**:
  - Time Complexity: O(n), as we iterate through the numbers up to `n`.
  - Space Complexity: O(1), as we use only three variables to store intermediate results.

## Edge Cases
- `n = 0`: Return 0.
- `n = 1`: Return 1.
- `n = 2`: Return 1.
- Large values of `n`: The iterative approach handles large `n` efficiently.

## Example Walkthrough
### Example 1:
- **Input**: `n = 4`
- **Process**:
  - Initialize `t0 = 0`, `t1 = 1`, `t2 = 1`.
  - Loop:
    - `t_next = t0 + t1 + t2 = 0 + 1 + 1 = 2`, update `t0 = 1`, `t1 = 1`, `t2 = 2`.
    - `t_next = t0 + t1 + t2 = 1 + 1 + 2 = 4`, update `t0 = 1`, `t1 = 2`, `t2 = 4`.
  - Return `t2 = 4`.
- **Output**: `4`

### Example 2:
- **Input**: `n = 25`
- **Process**:
  - The loop calculates the Tribonacci numbers iteratively up to `n = 25`.
  - Final value: `1389537`.
- **Output**: `1389537`

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!