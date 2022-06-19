class Solution:
    """
    >>> obj = Solution()
    >>> obj.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])
    2
    >>> obj.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
    2.5
    """

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_sorted = nums1 + nums2
        merged_sorted.sort()
        if len(merged_sorted) % 2 == 1:
            return merged_sorted[int(len(merged_sorted)/2)]

        half = int(len(merged_sorted)/2)
        return (merged_sorted[half]+merged_sorted[half-1])/2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
