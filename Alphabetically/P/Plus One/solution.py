## 66. Plus One
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # interate through the array, select each element turn it to str and concat it with the next
        num_str = ''.join(str(digit) for digit in digits)
        # once done with the loop, turn that string to integer, add one 
        incremented_num = int(num_str) + 1
        # turn it back to str and then split
        result = [int(digit) for digit in str(incremented_num)]

        return result 