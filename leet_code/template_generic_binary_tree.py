from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


def convert_list_to_tree(l):
    data = iter(l)
    tree = TreeNode(val=next(data))
    fringe = deque([tree])
    while True:
        print(fringe)
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
    def function(self, arg):
        return arg

if __name__ == '__main__':
    solution = Solution()
    print(solution.function('Hello World'))