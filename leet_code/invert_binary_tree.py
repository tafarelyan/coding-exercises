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
    # DFS solution
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root

    # BFS solution
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        visited = [root]
        while visited:
            node = visited.pop()

            node.left, node.right = node.right, node.left

            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)

        return root

if __name__ == '__main__':
    solution = Solution()

    root = convert_list_to_tree([4,2,7,1,3,6,9])
    print(root)
    print(solution.invertTree(root))