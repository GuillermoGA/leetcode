class Solution:
    """
    >>> obj = Solution()
    >>> obj.isPalindrome(424)
    True
    >>> obj.isPalindrome(-42)
    False
    """

    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
