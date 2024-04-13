class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->{self.next}'

def convert_list_to_linked_list(list_: list) -> ListNode:
    currentNode = None
    for val in list_[::-1]:
        node = ListNode(val=val, next=currentNode)
        currentNode = node
    return currentNode

#=============================================#

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length # avoid useless repetitions
        if k == 0:
            return head

        currentNode = head
        for _ in range(length - k - 1):
            currentNode = currentNode.next

        newHead = currentNode.next
        currentNode.next = None
        tail.next = head

        return newHead


if __name__ == '__main__':
    head = convert_list_to_linked_list([1,2,3,4,5])

    solution = Solution()
    solution.rotateRight(head, 2)