class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        # BFS
        output = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level.append(node.val)

            output.append(sum(level) / len(level))
        
        return output
                

    def averageOfLevels2(self, root: TreeNode) -> list:
        # DFS
        S = defaultdict(float)
        T = defaultdict(int)

        def dfs(node, h):
            if not node: return
            dfs(node.left, h+1)
            dfs(node.right,h+1)
            S[h] += node.val
            T[h] += 1

        dfs(root, 0)

        return [
            S[i] / T[i]
            for i in range(len(S))
        ]

if __name__ == '__main__':
    solution = Solution()
    node1 = TreeNode(val=3)
    node2 = TreeNode(val=9)
    node3 = TreeNode(val=20)
    node4 = TreeNode(val=15)
    node5 = TreeNode(val=7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    print(solution.averageOfLevels(node1))