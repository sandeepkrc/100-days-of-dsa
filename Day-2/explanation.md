# Power of Two — Explanation

## Problem
Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two if there exists an integer `x` such that `n == 2^x`.

## Current Solution
The current solution uses a loop to repeatedly divide the number by 2 while checking if it is divisible by 2. If at any point the number is not divisible by 2 (and not equal to 1), the function returns `false`. Otherwise, if the number reduces to 1, it returns `true`.

### Steps:
1. If `n <= 0`, return `false` (negative numbers and zero cannot be powers of two).
2. If `n == 1`, return `true` (since `2^0 = 1`).
3. While `n > 0`:
   - Check if `n % 2 != 0` and `n != 1`. If true, return `false`.
   - Otherwise, divide `n` by 2.
4. If the loop completes and `n == 1`, return `true`.

### Complexity:
- **Time Complexity**: O(log n), where `n` is the input number. This is because the number is divided by 2 in each iteration.
- **Space Complexity**: O(1), as no additional space is used.

### Edge Cases:
- `n = 0`: Return `false` (not a power of two).
- `n = 1`: Return `true` (2^0 = 1).
- `n = -2`: Return `false` (negative numbers cannot be powers of two).
- Large powers of two (e.g., `n = 2^30`): Should return `true`.

## Example Walkthrough
### Example 1:
- **Input**: `n = 16`
- **Process**:
  - `16 % 2 == 0`, divide by 2 → `n = 8`
  - `8 % 2 == 0`, divide by 2 → `n = 4`
  - `4 % 2 == 0`, divide by 2 → `n = 2`
  - `2 % 2 == 0`, divide by 2 → `n = 1`
- **Output**: `true`

### Example 2:
- **Input**: `n = 3`
- **Process**:
  - `3 % 2 != 0`, return `false`.
- **Output**: `false`

## Alternative Solution (Bitwise Approach)
We can use a bitwise operation to check if `n` is a power of two. A number is a power of two if it has exactly one `1` bit in its binary representation. For example:
- `2 (10 in binary)`
- `4 (100 in binary)`
- `8 (1000 in binary)`

### Approach:
1. Check if `n > 0`.
2. Use the expression `n & (n - 1) == 0` to determine if `n` is a power of two.
   - `n & (n - 1)` clears the lowest set bit of `n`. If the result is `0`, then `n` is a power of two.

### Complexity:
- **Time Complexity**: O(1), as the bitwise operation is constant time.
- **Space Complexity**: O(1).

### Example Walkthrough (Bitwise):
- **Input**: `n = 16`
  - `16 & (16 - 1) = 16 & 15 = 0`
- **Output**: `true`

- **Input**: `n = 3`
  - `3 & (3 - 1) = 3 & 2 = 2`
- **Output**: `false`

📘 Pseudo-code for n = 4
##
Input: n = 4
Binary of n:        0100
Binary of n - 1:    0011

Compute: n & (n - 1)
          0100
        & 0011
        --------
          0000

Check conditions:
n > 0 → true
(n & (n - 1)) == 0 → true

Result: TRUE (4 is a power of two)
📘 Pseudo-code for n = 7
Input: n = 7
Binary of n:        0111
Binary of n - 1:    0110

Compute: n & (n - 1)
          0111
        & 0110
        --------
          0110   (not zero)

Check conditions:
n > 0 → true
(n & (n - 1)) == 0 → false

Result: FALSE (7 is NOT a power of two)


---

Both solutions are valid, but the bitwise approach is more efficient and concise. It is recommended for scenarios where performance is critical.