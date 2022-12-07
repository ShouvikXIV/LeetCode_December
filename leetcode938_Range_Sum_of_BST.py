# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search(curr,arr):
    while not curr:
        return arr
    arr.append(curr.val)
    search(curr.right,arr)
    search(curr.left,arr)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        curr = root
        search(curr,arr)
        # print(arr)
        sum = 0
        for i in arr:
            if low<=i<=high:
                sum+=i
        return sum