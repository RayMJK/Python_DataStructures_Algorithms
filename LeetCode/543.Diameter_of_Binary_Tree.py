class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.ans = max(self.ans, left + right)

            return max(left, right) + 1

        depth(root)

        return self.ans
