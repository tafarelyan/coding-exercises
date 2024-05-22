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
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next

        currentNode.next = list1 or list2

        return dummy.next

if __name__ == '__main__':
    solution = Solution()

    node11 = ListNode(val=1)
    node12 = ListNode(val=2)
    node11.next = node12
    node13 = ListNode(val=4)
    node12.next = node13

    node21 = ListNode(val=1)
    node22 = ListNode(val=3)
    node21.next = node22
    node23 = ListNode(val=4)
    node22.next = node23

    print(solution.mergeTwoLists(node11, node21))