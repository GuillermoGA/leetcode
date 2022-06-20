class Solution:
    """
    >>> obj = Solution()
    >>> obj.isValid("()")
    True
    >>> obj.isValid("()[]{}")
    True
    >>> obj.isValid("(]")
    False
    """

    def isValid(self, s: str) -> bool:
        open_list = []

        for char in s:
            if char == "(":
                open_list.append(")")  # Parenthesis
            elif char == "[":
                open_list.append("]")  # Brackets
            elif char == "{":
                open_list.append("}")  # Key

            elif char in [")", "]", "}"]:
                if not open_list: # Starts with close
                    return False
                elif open_list[-1] != char: # Not match last open
                    return False
                else:
                    open_list.pop()  # remove closed char

        if open_list:  # still opened
            return False

        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
