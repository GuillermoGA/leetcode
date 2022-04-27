class Solution:
    """
    >>> obj = Solution()
    >>> obj.romanToInt("III")
    3
    >>> obj.romanToInt("MCMXCIV")
    1994
    """

    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # parse to upper
        s = s.upper()

        total = 0
        prev_letter = None
        current_letter = None
        for letter in reversed(s):
            current_letter = letter

            # To substract cases
            if current_letter == "C" and prev_letter in ["D", "M"]:
                total -= roman_to_int_dict[current_letter]
            elif current_letter == "X" and prev_letter in ["L", "C"]:
                total -= roman_to_int_dict[current_letter]
            elif current_letter == "I" and prev_letter in ["V", "X"]:
                total -= roman_to_int_dict[current_letter]
            else:
                # else add
                total += roman_to_int_dict[current_letter]

            prev_letter = current_letter

        return total


if __name__ == "__main__":
    import doctest
    doctest.testmod()
