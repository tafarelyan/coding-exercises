class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->{self.next}'

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        currentNode = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                currentNode.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                currentNode.next = ListNode(val=list2.val)
                list2 = list2.next

            currentNode = currentNode.next
            
        if list1:
            currentNode.next = list1
        elif list2:
            currentNode.next = list2

        return dummy.next


def convert_list_to_linked_list(list_: list) -> ListNode:
    currentNode = None
    for val in list_[::-1]:
        node = ListNode(val=val, next=currentNode)
        currentNode = node
    return currentNode

if __name__ == '__main__':
    solution = Solution()

    head1 = convert_list_to_linked_list([1,2,4])
    head2 = convert_list_to_linked_list([1,3,4])

    head = solution.mergeTwoLists(head1, head2)
    print(head)