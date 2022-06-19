import string


class Solution:
    """
    >>> obj = Solution()
    >>> obj.myAtoi("42")
    42
    >>> obj.myAtoi("   -42")
    -42
    >>> obj.myAtoi("4193 with words")
    4193
    >>> obj.myAtoi("words and 987")
    0
    >>> obj.myAtoi("2147483648")
    2147483647
    """

    def myAtoi(self, s: str) -> int:
        # Remove whitespaces
        s = s.strip()

        is_negative = False
        if s[0] == "-":
            is_negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        end_index = len(s)
        for index, letter in enumerate(s):
            if letter not in string.digits:
                end_index = index
                break

        s = s[:end_index]

        if not s:
            return 0

        if is_negative:
            s = "-" + s

        s = int(s)

        if s <= -2**31:
            return -2**31
        if 2**31-1 <= s:
            return 2**31-1
        return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
