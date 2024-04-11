class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        total = 0
        l = []
        while True:
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next

            l.append(total % 10)
            total = total // 10

            if not l1 and not l2 and not total:
                break

        head = None
        for n in l[::-1]:
            node = ListNode(val=n, next=head)
            head = node
        return head


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