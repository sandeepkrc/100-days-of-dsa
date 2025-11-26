# Two Sum II — Explanation

## Problem
Find two numbers in a sorted array that add up to a target. Return their 1-based indices.

## Approach
### Two-Pointer Technique
- Use two pointers: one at the start, one at the end.
- If the sum of the two numbers equals the target, return their indices.
- If the sum is less than the target, move the start pointer forward.
- If the sum is greater, move the end pointer backward.

### Complexity
- **Time**: O(n), single pass.
- **Space**: O(1), no extra space.

## Example
### Input: `numbers = [2, 7, 11, 15]`, `target = 9`
- Start = 0, End = 3.
- `numbers[0] + numbers[3] = 2 + 15 = 17 > 9`, move End.
- `numbers[0] + numbers[2] = 2 + 11 = 13 > 9`, move End.
- `numbers[0] + numbers[1] = 2 + 7 = 9`, return `[1, 2]`.

---

Simple and efficient!