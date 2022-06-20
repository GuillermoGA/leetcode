from typing import List


class Solution:
    """
    >>> obj = Solution()
    >>> obj.letterCombinations("23")
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    >>> obj.letterCombinations("")
    []
    >>> obj.letterCombinations("2")
    ['a', 'b', 'c']
    """

    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        combinations = []

        for digit in digits:
            next_combinations = []

            if not combinations:
                combinations = digit_letters[digit]
                continue

            for combination in combinations:
                for letter in digit_letters[digit]:
                    next_combinations.append(combination+letter)

            combinations = next_combinations

        return sorted(combinations)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
