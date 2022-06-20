from typing import List

class Solution:
    """
    >>> obj = Solution()
    >>> obj.threeSum([-1,0,1,2,-1,-4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> obj.threeSum([])
    []
    >>> obj.threeSum([0])
    []
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                for k in range(len(nums)):
                    if i == k or j == k:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in triplets:
                            triplets.append(triplet)

        return sorted(triplets)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
