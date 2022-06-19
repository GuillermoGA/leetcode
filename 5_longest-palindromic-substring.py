class Solution:
    """
    >>> obj = Solution()
    >>> obj.longestPalindrome("babad")
    'bab'
    >>> obj.longestPalindrome("cbbd")
    'bb'
    >>> obj.longestPalindrome("aacabdkacaa")
    'aca'
    >>> obj.longestPalindrome("a")
    'a'
    """
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        current_longest = ""
        for i in range(len(s)):
            for j in range(len(s)):
                current_longest = s[i:j+1]
                if current_longest[::-1] == current_longest and len(current_longest) > len(longest):
                    longest = current_longest
        return longest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
