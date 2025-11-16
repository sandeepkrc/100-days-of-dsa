class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            first = 0
            second = 1
            for i in range(2, n+1):
                third = first + second
                first = second
                second = third
            return second
    def fibRecursive(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fibRecursive(n-1) + self.fibRecursive(n-2)
        

sol = Solution()
print(sol.fib(2))  # 1
print(sol.fib(3))  # 2
print(sol.fib(4))  # 3

print(sol.fibRecursive(2))  # 1
print(sol.fibRecursive(3))  # 2
print(sol.fibRecursive(4))  # 3
print(sol.fib(10))  # 55
print(sol.fibRecursive(10))  # 55
