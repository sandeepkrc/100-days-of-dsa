# Container With Most Water — Explanation

## Problem Statement
You are given an integer array `height` of length `n`. Each element represents the height of a vertical line drawn at that index. The task is to find two lines that, together with the x-axis, form a container such that the container holds the most water. Return the maximum amount of water a container can store.

### Problem Details:
- The width of the container is the distance between the two lines.
- The height of the container is determined by the shorter of the two lines.
- The goal is to maximize the area of the container.

## Approach
### Two-Pointer Technique
- **Idea**: Use two pointers, one starting at the leftmost line and the other at the rightmost line. Gradually move the pointers inward to find the maximum area.
- **Steps**:
  1. Initialize two pointers: `left` at the start of the array and `right` at the end.
  2. Calculate the area formed by the lines at `left` and `right`.
  3. Update the maximum area if the current area is larger.
  4. Move the pointer pointing to the shorter line inward, as the height of the shorter line limits the area.
  5. Repeat until the pointers meet.

### Complexity
- **Time Complexity**: O(n), as we traverse the array once.
- **Space Complexity**: O(1), as we use only a constant amount of extra space.

## Edge Cases
- Array contains only two elements: The result is the area formed by those two lines.
- All elements are the same: The result is determined by the width of the array.
- Array contains zeros: Zeros do not contribute to the area.

## Example Walkthrough
### Example 1:
- **Input**: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- **Process**:
  - Start with `left = 0` and `right = 8`.
  - Calculate area: `min(1, 7) * (8 - 0) = 7`.
  - Move `left` to `1` (since `1 < 7`).
  - Repeat until `left` meets `right`, updating the maximum area.
- **Output**: `49`

### Example 2:
- **Input**: `height = [1, 1]`
- **Process**:
  - Start with `left = 0` and `right = 1`.
  - Calculate area: `min(1, 1) * (1 - 0) = 1`.
  - Pointers meet.
- **Output**: `1`

---

This explanation provides a clear understanding of the problem, the two-pointer technique, and the reasoning behind each step. Happy coding!
