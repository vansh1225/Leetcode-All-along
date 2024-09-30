# 26. Remove Duplicates from Sorted Array

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
        
