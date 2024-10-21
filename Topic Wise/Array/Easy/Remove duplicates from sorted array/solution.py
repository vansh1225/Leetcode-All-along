# 26. Remove Duplicates from Sorted Array - The goal is to remove duplicates from the list nums and return how many unique elements remain, which is the length of new nums.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            j= i + 1
            while j< len(nums):
                if nums[i] == nums[j]:
                    nums.remove(nums[j])
                else:
                    j+=1
        k=len(nums)
        return k
        
