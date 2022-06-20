from tabnanny import check


class Solution:
    """
    >>> obj = Solution()
    >>> obj.longestCommonPrefix(["flower","flow","flight"])
    'fl'
    >>> obj.longestCommonPrefix(["dog","racecar","car"])
    ''
    """

    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        letter_index = 0
        for letter_index in range(len(min(strs))):
            check_letter = strs[0][letter_index]
            match = True
            for word in strs[1:]:
                if word[letter_index] != check_letter:
                    match = False
                    break
            if match:
                prefix += check_letter
            else:
                break

        return prefix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
