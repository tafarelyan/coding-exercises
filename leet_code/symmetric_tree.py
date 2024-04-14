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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False

        left_queue, right_queue = [root.left], [root.right]

        while left_queue and right_queue:
            left = left_queue.pop()
            right = right_queue.pop()

            if left.val != right.val:
                return False

            if left.left and right.right:
                left_queue.append(left.left)
                right_queue.append(right.right)
            elif left.left or right.right:
                return False

            if left.right and right.left:
                left_queue.append(left.right)
                right_queue.append(right.left)
            elif left.right or right.left:
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    root = convert_list_to_tree([1,2,2,3,4,4,3])
    print(solution.isSymmetric(root))
    root = convert_list_to_tree([1,2,2,None,3,None,3])
    print(solution.isSymmetric(root))