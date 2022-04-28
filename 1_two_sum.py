class Solution:
    """
    >>> obj = Solution()
    >>> obj.twoSum(nums = [2,7,11,15], target = 9)
    [0, 1]
    >>> obj.twoSum(nums = [3,2,4], target = 6)
    [1, 2]
    >>> obj.twoSum(nums = [3,3], target = 6)
    [0, 1]
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if target == nums[i] + nums[j]:
                    return [i, j]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
