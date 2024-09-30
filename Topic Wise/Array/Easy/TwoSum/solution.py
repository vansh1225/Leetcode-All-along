# 1. Two Sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # stored_indices = {}
        # for i, num in enumerate(nums):#2,7,11,15
        #     component = target - num
        #     if component in stored_indices:
        #         return [stored_indices[component], i]
        #     stored_indices[num] = i
        # return []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []