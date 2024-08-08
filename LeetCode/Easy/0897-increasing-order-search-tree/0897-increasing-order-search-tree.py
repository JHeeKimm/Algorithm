# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, nodes):
            if node:
                inorder(node.left, nodes)
                nodes.append(node)
                inorder(node.right, nodes)
        nodes = []
        inorder(root, nodes)
        
        new_root = nodes[0]
        current = new_root
        current.left = None
        
        for node in nodes[1:]:
            node.left = None
            current.right = node
            current = current.right
            
        current.right = None
        
        return new_root