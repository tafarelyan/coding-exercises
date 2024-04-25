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
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, number):
            if not node:
                return 0

            number = number * 10 + node.val
            if not node.left and not node.right:
                return number

            return dfs(node.left, number) + dfs(node.right, number)

        return dfs(root, 0)

if __name__ == '__main__':
    solution = Solution()

    root = convert_list_to_tree([1,2,3])
    print(solution.sumNumbers(root))