class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        currentNode = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            currentNode.next = ListNode(val=val)

            currentNode = currentNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def convert_list_to_linked_list(l):
    head = None
    for n in l[::-1]:
        node = ListNode(val=n, next=head)
        head = node
    return head

def print_linked_list(head):
    currentNode = head
    while currentNode:
        print(currentNode.val, end='->')
        currentNode = currentNode.next
    print('None')

if __name__ == '__main__':
    solution = Solution()

    l1 = convert_list_to_linked_list([2,4,3])
    l2 = convert_list_to_linked_list([5,6,4])
    head = solution.addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = convert_list_to_linked_list([0])
    l2 = convert_list_to_linked_list([0])
    head = solution.addTwoNumbers(l1, l2)
    print_linked_list(head)

    l1 = convert_list_to_linked_list([9,9,9,9,9,9,9])
    l2 = convert_list_to_linked_list([9,9,9,9])
    head = solution.addTwoNumbers(l1, l2)
    print_linked_list(head)