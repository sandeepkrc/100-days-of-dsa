
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Given a string s, remove duplicate letters so that every letter appears once and only once.
        You must make sure your result is the smallest in lexicographical order among all possible results.
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return ''.join(stack)
    
# time complexity: O(n), where n is the length of the string s
# space complexity: O(k), where k is the number of unique characters in s
solution = Solution()
# Example usage
print(solution.removeDuplicateLetters("bcabc"))  # Output: "abc"
print(solution.removeDuplicateLetters("cbacdcbc"))  # Output: "acdb"
print(solution.removeDuplicateLetters("abacb"))  # Output: "abc"

        

        