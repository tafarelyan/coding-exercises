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
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def dfs(node, max_value):
            if not node:
                return

            if node.val >= max_value:
                count[0] += 1

            dfs(node.left, max(node.val, max_value))
            dfs(node.right, max(node.val, max_value))

        dfs(root, root.val)
        return count[0]

if __name__ == '__main__':
    solution = Solution()
    root = convert_list_to_tree([3,1,4,3,None,1,5])
    print(solution.goodNodes(root))

    root = convert_list_to_tree([3,3,None,4,2])
    print(solution.goodNodes(root))

    root = convert_list_to_tree([1])
    print(solution.goodNodes(root))