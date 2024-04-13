from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'<{self.val}>'

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # BFS solution
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        visited = [(p, q)]
        while visited:
            nodeP, nodeQ = visited.pop()

            if nodeP.val != nodeQ.val:
                return False

            if nodeP.left and nodeQ.left:
                visited.append((nodeP.left, nodeQ.left))
            elif nodeP.left or nodeQ.left:
                return False

            if nodeP.right and nodeQ.right:
                visited.append((nodeP.right, nodeQ.right))
            elif nodeP.right or nodeQ.right:
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    p = convert_list_to_tree([1,2,3])
    q = convert_list_to_tree([1,2,3])

    print(solution.isSameTree(p, q))