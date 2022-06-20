from typing import List


class Solution:
    """
    >>> obj = Solution()
    >>> obj.threeSumClosest(nums = [-1,2,1,-4], target = 1)
    2
    >>> obj.threeSumClosest(nums = [0,0,0], target = 1)
    0
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = sum(nums[:3])
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                for k in range(len(nums)):
                    if i == k or j == k:
                        continue

                    current_sum = nums[i] + nums[j] + nums[k]
                    if abs(current_sum - target) <= abs(closest - target):
                        closest = current_sum

        return closest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
