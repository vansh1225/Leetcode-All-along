# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # type: ignore
        # Base case: if the array is empty, return None (no tree)
        if not nums:
            return None
        
        # Find the middle index
        mid = len(nums) // 2
        
        # Create a TreeNode with the middle element as the root
        root = TreeNode(nums[mid]) # type: ignore
        
        # Recursively construct the left subtree using the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively construct the right subtree using the right half of the array
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
