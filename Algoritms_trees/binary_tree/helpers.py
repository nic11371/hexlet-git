from tree_node import BinaryTreeNode

def sorted_array_to_BST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = BinaryTreeNode(nums[mid])
    root.left = sorted_array_to_BST(nums[:mid])
    root.right = sorted_array_to_BST(nums[mid+1:])
    
    return root
