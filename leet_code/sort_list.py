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
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode(val=0)
        currentNode = dummy
        while left and right:
            if left.val < right.val:
                currentNode.next = left
                left = left.next
            else:
                currentNode.next = right
                right = right.next

            currentNode = currentNode.next

        currentNode.next = left or right

        return dummy.next

if __name__ == '__main__':
    solution = Solution()

    head = convert_list_to_linked_list([4,2,1,3])
    print(solution.sortList(head))