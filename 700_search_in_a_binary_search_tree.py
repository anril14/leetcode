from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None

        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return TreeNode(root.val, root.left, root.right)

node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2, node1, node3)
node7 = TreeNode(7)
node4 = TreeNode(4, node2, node7)

solution = Solution()
print(solution.searchBST(node4, 3))