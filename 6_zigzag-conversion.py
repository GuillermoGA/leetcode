class Solution:
    """
    >>> obj = Solution()
    >>> obj.convert(s = "PAYPALISHIRING", numRows = 3)
    'PAHNAPLSIIGYIR'
    >>> obj.convert(s = "PAYPALISHIRING", numRows = 4)
    'PINALSIGYAHRPI'
    >>> obj.convert(s = "A", numRows = 1)
    'A'
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        # create matrix with numRows rows
        matrix = []
        for _ in range(numRows):
            matrix.append([])

        current_row = 0
        going_down = False

        for letter in s:
            matrix[current_row] += letter

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        # Flat matrix
        final_string = ""
        for m_list in matrix:
            final_string += "".join(m_list)

        return final_string


if __name__ == "__main__":
    import doctest
    doctest.testmod()
