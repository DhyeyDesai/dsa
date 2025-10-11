# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Intuition: 
#   - Use backtracking to explore all possible letter combinations.
#   - For each digit, try each of its corresponding letters, then recursively
#   move to the next digit. Build up the combination string as we go deeper.
# Time Complexity: O(4^n * n) where n is the length of digits
#   - 4^n combinations in worst case (digits 7 and 9 have 4 letters)
#   - n for string concatenation at each step
# Space Complexity: O(n) for recursion call stack depth (not counting output)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        # Map each digit to its corresponding letters on a phone keypad
        keypad_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        
        def backtrack(index, path ):
            # Base case: if we've processed all digits, add the combination to result
            if index == len(digits):
                result.append(path)
                return

            # Recursive case: try each letter corresponding to the current digit
            for char in keypad_map[digits[index]]:
                # Move to next digit with current letter added to path
                backtrack(index+1, path+char)



        # Start backtracking from index 0 with an empty path
        backtrack(0, "")
        return result
        