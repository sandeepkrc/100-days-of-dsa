# Median of Two Sorted Arrays — Explanation

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(m + n).

### Problem Details:
- The median is the middle value in an ordered list of numbers.
- If the total number of elements is even, the median is the average of the two middle values.
- The arrays are sorted, which allows for efficient merging.

## Approach
### Merge and Find Median
- **Idea**: Merge the two sorted arrays into one sorted array and then find the median of the merged array.
- **Steps**:
  1. Use a helper function `merge_arrays` to merge `nums1` and `nums2` into a single sorted array.
     - Use two pointers to traverse both arrays.
     - Compare elements from both arrays and append the smaller one to the merged array.
     - If one array is exhausted, append the remaining elements of the other array.
  2. Once the arrays are merged, calculate the median:
     - If the total number of elements is odd, the median is the middle element.
     - If the total number of elements is even, the median is the average of the two middle elements.

### Complexity Analysis:
- **Time Complexity**: O(m + n), where `m` and `n` are the sizes of `nums1` and `nums2`. This is because we traverse both arrays once during the merge process.
- **Space Complexity**: O(m + n), as we create a new array to store the merged result.

## Edge Cases
- One array is empty: The median is the median of the non-empty array.
- Arrays of different sizes: The approach handles arrays of unequal lengths seamlessly.
- Arrays with duplicate elements: The approach works correctly as duplicates are treated like any other elements.

## Example Walkthrough
### Example 1:
- **Input**: `nums1 = [1, 3]`, `nums2 = [2]`
- **Process**:
  - Merge the arrays: `merged = [1, 2, 3]`.
  - Total elements = 3 (odd), median = middle element = `2`.
- **Output**: `2`

### Example 2:
- **Input**: `nums1 = [1, 2]`, `nums2 = [3, 4]`
- **Process**:
  - Merge the arrays: `merged = [1, 2, 3, 4]`.
  - Total elements = 4 (even), median = average of middle elements = `(2 + 3) / 2 = 2.5`.
- **Output**: `2.5`

### Example 3:
- **Input**: `nums1 = [0, 0]`, `nums2 = [0, 0]`
- **Process**:
  - Merge the arrays: `merged = [0, 0, 0, 0]`.
  - Total elements = 4 (even), median = average of middle elements = `(0 + 0) / 2 = 0`.
- **Output**: `0`

---

This explanation provides a clear understanding of the problem, the approach used to solve it, and the reasoning behind each step. Happy coding!