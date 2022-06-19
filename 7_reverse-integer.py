class Solution:
    """
    >>> obj = Solution()
    >>> obj.reverse(123)
    321
    >>> obj.reverse(-123)
    -321
    >>> obj.reverse(120)
    21
    """
    def reverse(self, x: int) -> int:     
        str_x = str(x)
        negative = str_x[0] == "-"
        
        if negative:
            str_x = str_x[1:]
            
        str_x = str_x[::-1]
        
        if negative:
            str_x = "-" + str_x
            
        reversed_x = int(str_x)
    
        # Return 0 for non 32 bit integer
        if not -2**31 <= reversed_x <= 2**31-1:
            return 0
        
        return reversed_x
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()

        