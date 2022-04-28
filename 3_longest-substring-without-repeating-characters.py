class Solution:
    """
    >>> obj = Solution()
    >>> obj.lengthOfLongestSubstring("dvdf")
    3
    >>> obj.lengthOfLongestSubstring("asjrgapa")
    6
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        count = 0
        for char in s:
            if char in longest:
                longest = longest[longest.index(char)+1:]
            longest += char
            if count < len(longest):
                count = len(longest)

        return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
