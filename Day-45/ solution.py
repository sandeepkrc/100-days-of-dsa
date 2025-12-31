from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of words and spaces, return the length of the last word in the string.
        A word is a maximal substring consisting of non-space characters only.
        """
        # Strip trailing spaces and split the string into words
        words = s.strip().split()
        
        # If there are no words, return 0
        if not words:
            return 0
        
        # Return the length of the last word
        return len(words[-1])
    
# time complexity: O(n), where n is the length of the string s
# space complexity: O(n), for storing the list of words

solution = Solution()
# Example usage
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
print(solution.lengthOfLastWord("a"))  # Output: 1
print(solution.lengthOfLastWord(""))  # Output: 0