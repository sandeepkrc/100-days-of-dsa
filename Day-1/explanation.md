
# Palindrome Number — Explanation

Problem: Given an integer x, return true if x is a palindrome, and false otherwise.

This folder contains two common approaches to solve the problem: a string-based check and a numeric reverse check. Both are correct for the constraint range, but they differ in time/space trade-offs and implementation details.

## Approach 1 — String conversion (easy / concise)

Idea: Convert the integer to its decimal string and check whether the string reads the same forwards and backwards.

Steps:
- If x is negative, immediately return False (the minus sign makes it non-palindromic).
- Convert x to string: `s = str(x)`.
- Compare `s` to its reverse `s[::-1]` and return the boolean result.

Pros:
- Very short and easy to implement.
- Good for quick scripts and when readability matters.

Cons:
- Uses extra memory proportional to the number of digits (for the string and its reverse).
- Slight overhead from allocating and slicing strings.

Time Complexity: O(n), where n is the number of digits in the integer. This is because converting the integer to a string and checking if it is a palindrome both take linear time.
Space Complexity: O(n), as we are storing the string representation of the integer.


## Approach 2 — Reverse the integer numerically (no string)

Idea: Reverse the digits of the number using arithmetic and compare the reversed integer to the original.

Steps:
- If x is negative, return False.
- Keep a copy `original = x`.
- Build `reversed_num` by repeatedly taking the last digit `digit = x % 10`, then `reversed_num = reversed_num * 10 + digit`, and remove the last digit from x via integer division `x //= 10` until x becomes 0.
- Compare `original == reversed_num` and return the result.

Pros:
- Avoids converting to strings; uses constant extra space.
- Slightly more memory-efficient for very large inputs.

Cons / Caution:
- If the problem allowed values outside the 32-bit signed integer range and asked to reverse the integer, you'd need to check for overflow while building the reversed number. For this palindrome check, overflow isn't an issue because you compare the full reversed value to the original value (and the input is bounded by the problem constraints).


Time Complexity: O(n) where n is the number of digits in x because we reverse the digits 
Space Complexity: O(1) as we use only a constant amount of extra space

## Edge cases
- Negative numbers: always not palindrome (e.g., -121 -> False).
- Single digit numbers: always palindrome (0..9 -> True).
- Trailing zeros: numbers like 10 are not palindromes because reversing digits yields 01 -> 1 != 10.

## Example walkthrough (x = 121)

- String approach: `"121" == "121"[::-1]` -> True.
- Numeric approach: build reversed_num: 1 -> 12 -> 121. Compare to original 121 -> True.

## Recommendation / Notes

Both solutions in `solution.py` are valid. For interview or production code where you want to avoid unnecessary allocations and show numeric manipulation skills, prefer the numeric reverse approach. For short scripts or when clarity is preferred, the string approach is fine.

If you want an extra micro-optimization in the numeric approach, you can reverse only half of the digits and compare halves (that avoids completely reversing the number) — useful when avoiding overflow checks. But for the typical constraints (32-bit ints) and this problem, the simple numeric reverse is clear and fast.

---

Files in this folder:

- `solution.py` — contains two implementations: the string-based check and the numeric reverse check (both implemented as methods named `isPalindrome`).

Happy coding!

