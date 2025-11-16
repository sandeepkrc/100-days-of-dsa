# Fibonacci Number — Explanation

## Problem Statement
The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1. That is:

- F(0) = 0
- F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n > 1

Given an integer `n`, calculate `F(n)`.

## Approach
### Solution 1: Iterative Approach
- **Idea**: Use a loop to calculate Fibonacci numbers iteratively, storing only the last two numbers to save space.
- **Steps**:
  1. If `n == 0`, return 0.
  2. If `n == 1`, return 1.
  3. Initialize two variables, `first = 0` and `second = 1`.
  4. Use a loop from 2 to `n`, updating the variables to calculate the next Fibonacci number.
  5. Return the last calculated Fibonacci number.
- **Complexity**:
  - Time Complexity: O(n), as we iterate through the numbers up to `n`.
  - Space Complexity: O(1), as we use only two variables to store intermediate results.

### Solution 2: Recursive Approach
- **Idea**: Use recursion to calculate Fibonacci numbers based on the recurrence relation `F(n) = F(n-1) + F(n-2)`.
- **Steps**:
  1. If `n == 0`, return 0.
  2. If `n == 1`, return 1.
  3. Otherwise, return `fib(n-1) + fib(n-2)`.
- **Complexity**:
  - Time Complexity: O(2^n), as each call spawns two more calls, leading to exponential growth.
  - Space Complexity: O(n), due to the recursion stack.

### Comparison
- The iterative approach is more efficient and avoids the overhead of recursion.
- The recursive approach is simpler to implement but becomes impractical for large `n` due to its exponential time complexity.

## Edge Cases
- `n = 0`: Return 0.
- `n = 1`: Return 1.
- Large values of `n`: The iterative approach handles large `n` efficiently, while the recursive approach may cause a stack overflow.

## Example Walkthrough
### Example 1:
- **Input**: `n = 2`
- **Iterative Process**:
  - Initialize `first = 0`, `second = 1`.
  - Loop: `third = first + second = 0 + 1 = 1`.
  - Update: `first = 1`, `second = 1`.
  - Return `second = 1`.
- **Recursive Process**:
  - `fib(2) = fib(1) + fib(0) = 1 + 0 = 1`.
- **Output**: `1`

### Example 2:
- **Input**: `n = 4`
- **Iterative Process**:
  - Initialize `first = 0`, `second = 1`.
  - Loop:
    - `third = first + second = 0 + 1 = 1`, update `first = 1`, `second = 1`.
    - `third = first + second = 1 + 1 = 2`, update `first = 1`, `second = 2`.
    - `third = first + second = 1 + 2 = 3`, update `first = 2`, `second = 3`.
  - Return `second = 3`.
- **Recursive Process**:
  - `fib(4) = fib(3) + fib(2)`.
  - `fib(3) = fib(2) + fib(1)`.
  - `fib(2) = fib(1) + fib(0)`.
  - Combine results: `fib(4) = 3`.
- **Output**: `3`

---

This explanation provides a clear understanding of the problem, the approaches used to solve it, and the reasoning behind each step. Happy coding!