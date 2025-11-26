# Two Sum II — Explanation

## Problem Statement
Given a sorted array `numbers` and a target value `target`, find two numbers in the array that add up to `target`. Return their indices as a 1-based array.

## Approach
### Two-Pointer Technique
- **Idea**: Use two pointers, one starting at the beginning (`start`) and the other at the end (`end`) of the array. Adjust the pointers based on the sum of the elements at these positions.
- **Steps**:
  1. Initialize `start` to 0 and `end` to the last index of the array.
  2. While `start < end`:
     - Calculate the sum of `numbers[start]` and `numbers[end]`.
     - If the sum equals `target`, return `[start + 1, end + 1]`.
     - If the sum is less than `target`, increment `start`.
     - If the sum is greater than `target`, decrement `end`.

### Brute Force Approach
- **Idea**: Check all possible pairs of numbers in the array to find the pair that adds up to the target.
- **Steps**:
  1. Iterate through the array with two nested loops.
  2. For each pair of indices `(i, j)` where `i < j`, check if `numbers[i] + numbers[j] == target`.
  3. If a pair is found, return `[i + 1, j + 1]`.

### Complexity
- **Two-Pointer Technique**:
  - Time Complexity: O(n), where `n` is the length of the array. Each element is processed at most once.
  - Space Complexity: O(1), as no additional space is used.
- **Brute Force Approach**:
  - Time Complexity: O(n^2), as we check all pairs of elements.
  - Space Complexity: O(1), as no additional space is used.

## Example Walkthrough
### Example 1:
- **Input**: `numbers = [2, 7, 11, 15]`, `target = 9`
- **Two-Pointer Process**:
  - Initialize `start = 0`, `end = 3`.
  - `numbers[0] + numbers[3] = 2 + 15 = 17 > 9`, decrement `end`.
  - `numbers[0] + numbers[2] = 2 + 11 = 13 > 9`, decrement `end`.
  - `numbers[0] + numbers[1] = 2 + 7 = 9`, return `[1, 2]`.
- **Brute Force Process**:
  - Check pairs `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, etc.
  - Find that `numbers[0] + numbers[1] = 2 + 7 = 9`, return `[1, 2]`.
- **Output**: `[1, 2]`

### Example 2:
- **Input**: `numbers = [2, 3, 4]`, `target = 6`
- **Two-Pointer Process**:
  - Initialize `start = 0`, `end = 2`.
  - `numbers[0] + numbers[2] = 2 + 4 = 6`, return `[1, 3]`.
- **Brute Force Process**:
  - Check pairs `(0, 1)`, `(0, 2)`, `(1, 2)`.
  - Find that `numbers[0] + numbers[2] = 2 + 4 = 6`, return `[1, 3]`.
- **Output**: `[1, 3]`

### Example 3:
- **Input**: `numbers = [-1, 0]`, `target = -1`
- **Two-Pointer Process**:
  - Initialize `start = 0`, `end = 1`.
  - `numbers[0] + numbers[1] = -1 + 0 = -1`, return `[1, 2]`.
- **Brute Force Process**:
  - Check pair `(0, 1)`.
  - Find that `numbers[0] + numbers[1] = -1 + 0 = -1`, return `[1, 2]`.
- **Output**: `[1, 2]`

---

This explanation provides a clear and concise understanding of the problem, the two-pointer approach, and the brute force solution.
