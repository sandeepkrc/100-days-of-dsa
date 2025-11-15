class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 0:
            if n % 2 != 0 and n != 1:
                return False
            n = n // 2
            if n == 1:
                return True
        return False

    def isPowerOfTwoBitwise(self, n: int) -> bool:
        # Alternative solution using bitwise operations
        return n > 0 and (n & (n - 1)) == 0

sol = Solution()
print(sol.isPowerOfTwo(16))  # True
print(sol.isPowerOfTwo(3))   # False
print(sol.isPowerOfTwo(1))   # True
print(sol.isPowerOfTwo(0))   # False
print(sol.isPowerOfTwo(-2))  # False

# Testing the bitwise solution
print(sol.isPowerOfTwoBitwise(16))  # True
print(sol.isPowerOfTwoBitwise(3))   # False
print(sol.isPowerOfTwoBitwise(1))   # True
print(sol.isPowerOfTwoBitwise(0))   # False
print(sol.isPowerOfTwoBitwise(-2))  # False