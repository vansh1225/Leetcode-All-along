# 35. Search Insert Position

from typing import List


class Solution: # Time Complexity - O(LogN)
    def searchInsert(self, nums: List[int], target: int) -> int:
        #start
        #end
        #half = nums/2
        #if target == nums/2: return 
        #elseif target<nums/2 : end = half - 1 then do a one more half = n/2
        #elseif target>num/2 :  start = half + 1 then do a one more half = n/2
        start = 0
        end= len(nums) -1
        while start <= end:
            half = ( start + end ) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target :
                start = half + 1
            elif nums[half] > target :
                end = half - 1
        return start