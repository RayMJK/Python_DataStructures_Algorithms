# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level = 0
        curLevel = [root]
        nextLevel = []
        while curLevel:
            for i in range(len(curLevel)):
                cur = curLevel[i]
                if cur.left:
                    nextLevel.append(cur.left)
                if cur.right:
                    nextLevel.append(cur.right)
                if cur.val % 2 == level % 2:
                    return False
                if i > 0 and level%2 == 0 and cur.val <= curLevel[i-1].val:
                    return False
                if i > 0 and level%2 != 0 and cur.val >= curLevel[i-1].val:
                    return False
            curLevel = nextLevel
            nextLevel = []
            level += 1
        return True