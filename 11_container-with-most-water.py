class Solution:
    """
    >>> obj = Solution()
    >>> obj.maxArea([1,8,6,2,5,4,8,3,7])
    49
    >>> obj.maxArea([1,1])
    1
    """
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                current_height = min(height[i], height[j])
                current_base = j-i
                current_area = current_height * current_base

                if current_area > max_area:
                    max_area = current_area

        return max_area


if __name__ == "__main__":
    import doctest
    doctest.testmod()
