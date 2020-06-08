# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.avg_list = {}

    def solve(self, root, depth):
        if self.avg_list.get(depth)==None and (root.left != None or root.right != None):
            self.avg_list[depth] = [0, 0]
        if root.left != None:
            self.avg_list[depth][0] += root.left.val
            self.avg_list[depth][1] += 1
            self.solve(root.left, depth + 1)
        if root.right != None:
            self.avg_list[depth][0] += root.right.val
            self.avg_list[depth][1] += 1
            self.solve(root.right, depth + 1)

    def get_output(self):
        return [v[0] / v[1] for k, v in self.avg_list.items()]

    def averageOfLevels(self, root):
        self.solve(root, 1)
        return [root.val] + self.get_output()
