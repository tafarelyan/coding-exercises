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
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next

            head = head.next

        ltail.next = right.next
        rtail.next = None

        return left.next

if __name__ == '__main__':
    solution = Solution()
    head = convert_list_to_linked_list([1,4,3,2,5,2])
    print(solution.partition(head, 3))