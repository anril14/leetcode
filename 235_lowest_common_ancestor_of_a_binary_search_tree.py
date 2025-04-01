from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_roots = []
        q_roots = []

        def search(root_val, val, arr):
            if not root_val:
                return None
            arr.append(root_val)
            if val.val < root_val.val:
                return search(root_val.left, val, arr)
            elif val.val > root_val.val:
                return search(root_val.right, val, arr)
            else:
                return root_val.val

        search(root, p, p_roots)
        search(root, q, q_roots)
        # print(p_roots)
        # print(q_roots)

        for i in reversed(q_roots):
            for j in reversed(p_roots):
                if j == i:
                    return i


node3 = TreeNode(3)
node5 = TreeNode(5)
node4 = TreeNode(4, node3, node5)
node0 = TreeNode(0)
node7 = TreeNode(7)
node9 = TreeNode(9)
node8 = TreeNode(8, node7, node9)
node2 = TreeNode(2, node0, node4)
node6 = TreeNode(6, node2, node8)

solution = Solution()
print(solution.lowestCommonAncestor(node6, node4, node9).val)
