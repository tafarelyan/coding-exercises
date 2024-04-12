class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def function(self, arg):
        return arg


def convert_list_to_linked_list(list_: list) -> ListNode:
    currentNode = None
    for val in list_[::-1]:
        node = ListNode(val=val, next=currentNode)
        currentNode = node
    return currentNode

def print_linked_list(head: ListNode) -> None:
    currentNode = head
    while currentNode:
        print(currentNode.val, end='->')
        currentNode = currentNode.next
    print('None')

if __name__ == '__main__':
    solution = Solution()
    print(solution.function('Hello World'))