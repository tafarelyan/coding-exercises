from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'

def convert_list_to_tree(l: list) -> TreeNode:
    data = iter(l)
    tree = TreeNode(val=next(data))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            val = next(data)
            if val:
                head.left = TreeNode(val=val)
                fringe.append(head.left)
            val = next(data)
            if val:
                head.right = TreeNode(val=val)
                fringe.append(head.right)
        except StopIteration:
            break

    return tree

#========================================#

class Solution:
    def longestZigZag(self, root: TreeNode) -> TreeNode:
        self.max_distance = 0

        def dfs(node, left, right):
            self.max_distance = max(self.max_distance, left, right)

            if node.left:
                dfs(node.left, right+1, 0)
            if node.right:
                dfs(node.right, 0, left+1)

        dfs(root, 0, 0)
        return self.max_distance

if __name__ == '__main__':
    solution = Solution()
    root = convert_list_to_tree([1,None,2,3,3,None,None,4,4,None,5,None,None,None,7])
    print(solution.longestZigZag(root))