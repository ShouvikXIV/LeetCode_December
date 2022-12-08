# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(curr,arr):
    if not curr.right and not curr.left:
        arr.append(curr.val)
        return
    if curr.left and not curr.right:
        traverse(curr.left,arr)
    elif curr.right and not curr.left:
        traverse(curr.right,arr)
    elif curr.right and curr.left:
        traverse(curr.left,arr)
        traverse(curr.right,arr)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        curr1 = root1
        arr1 = []
        curr2 = root2
        arr2 = []
        traverse(curr1,arr1)
        traverse(curr2,arr2)
        # print(arr1)
        # print(arr2)
        return arr1 == arr2