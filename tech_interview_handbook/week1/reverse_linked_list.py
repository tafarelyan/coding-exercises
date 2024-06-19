class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->{self.next}'

def get_linked_list_from_list(l: list) -> ListNode:
    dummy = ListNode()
    currentNode = dummy
    for val in l:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next

    return dummy.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        arguments = [] 
        while head:
            arguments.append(head.val)
            head = head.next

        arguments.reverse()
        dummy = ListNode()
        currentNode = dummy
        for val in arguments:
            currentNode.next = ListNode(val)
            currentNode = currentNode.next

        return dummy.next

if __name__ == '__main__':
    solution = Solution()

    head = get_linked_list_from_list([1,2,3,4,5])

    print(solution.reverseList(head))