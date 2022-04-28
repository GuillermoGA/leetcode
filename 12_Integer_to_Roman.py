class Solution:
    """
    >>> obj = Solution()
    >>> obj.intToroman_num(3)
    'III'
    >>> obj.intToroman_num(1994)
    'MCMXCIV'
    """

    def intToRoman(self, num: int) -> str:
        int_to_roman_num_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        roman_num = ""
        unit = 1
        for char_num in reversed(str(num)):
            digit = int(char_num)

            # handle subtraction cases 9, 90, 900
            if digit == 9:
                roman_num = int_to_roman_num_dict[unit] + \
                    int_to_roman_num_dict[10 * unit] + roman_num

            # handle digits that require a V/L/D
            elif digit >= 5:
                for i in range(0, digit - 5):
                    roman_num = int_to_roman_num_dict[unit] + roman_num
                roman_num = int_to_roman_num_dict[5 * unit] + roman_num

            # handle subtraction cases 4, 40, 400
            elif digit == 4:
                roman_num = int_to_roman_num_dict[unit] + \
                    int_to_roman_num_dict[5 * unit] + roman_num

            # handle numbers that can be formed from I/X/C/M only
            else:
                for i in range(0, digit):
                    roman_num = int_to_roman_num_dict[unit] + roman_num

            unit *= 10

        return roman_num


if __name__ == "__main__":
    import doctest
    doctest.testmod()
