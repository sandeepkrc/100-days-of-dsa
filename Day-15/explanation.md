# Bulb Switcher — Explanation

## Problem Statement
There are `n` bulbs that are initially turned off. You first turn on all the bulbs, then you turn off every second bulb. On the third round, you toggle every third bulb (turn it on if it's off, or turn it off if it's on). For the `i-th` round, you toggle every `i-th` bulb. Return the number of bulbs that are on after `n` rounds.

### Problem Details:
- Bulbs are toggled multiple times based on their position.
- A bulb ends up being on if it is toggled an odd number of times.
- A bulb is toggled on every divisor of its position.

## Approach
### Key Insight
A bulb will remain on if it is toggled an odd number of times. This happens only when the bulb's position is a perfect square. For example:
- Position 1: Divisors are [1] → Odd count → Bulb is ON.
- Position 4: Divisors are [1, 2, 4] → Odd count → Bulb is ON.
- Position 6: Divisors are [1, 2, 3, 6] → Even count → Bulb is OFF.

### Simplified Solution
- The number of bulbs that remain on corresponds to the number of perfect squares less than or equal to `n`.
- To find this, calculate the integer square root of `n`.

### Steps
1. Initialize a counter `count` to 0.
2. Iterate through numbers starting from 1, and for each number, check if its square is less than or equal to `n`.
3. Increment the counter for each valid number.
4. Return the counter.

### Complexity
- **Time Complexity**: O(√n), as we iterate through numbers up to the square root of `n`.
- **Space Complexity**: O(1), as we use only a constant amount of extra space.

## Example Walkthrough
### Example 1:
- **Input**: `n = 3`
- **Process**:
  - Perfect squares ≤ 3: [1].
- **Output**: `1`

### Example 2:
- **Input**: `n = 0`
- **Process**:
  - Perfect squares ≤ 0: [].
- **Output**: `0`

### Example 3:
- **Input**: `n = 1`
- **Process**:
  - Perfect squares ≤ 1: [1].
- **Output**: `1`

---

This explanation simplifies the problem and provides a clear understanding of the solution. Happy coding!
