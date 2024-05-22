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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, total):
            if not node:
                return False

            total += node.val
            if not node.left and not node.right:
                return total == targetSum

            return dfs(node.left, total) or dfs(node.right, total)

        return dfs(root, 0)

if __name__ == '__main__':
    solution = Solution()
    
    root = convert_list_to_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(solution.hasPathSum(root, 22))