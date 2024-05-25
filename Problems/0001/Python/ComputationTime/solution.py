from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = dict()
        for i, num in enumerate(nums):
            if num in complement:
                return complement[num], i
            else:
                complement[target - num] = i
        return None