# 27. Remove Element - Basically yu are given an array and also a value that needs to be removed from it.

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # This pointer will keep track of the position for non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to the front
                k += 1  # Increment k to indicate the next position for non-val elements
        return k
