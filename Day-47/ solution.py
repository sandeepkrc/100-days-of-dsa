class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
# Example usage:
solution = Solution()
input_str = "the sky is blue"
output_str = solution.reverseWords(input_str)
print(output_str)  # Output: "blue is sky the"