class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break

                currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, '->', end=' ')
            currentNode = currentNode.nextNode

        print('None')

if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.insert(16)
    llist.insert(13)
    llist.insert(7)

    data = 1
    position = 2

    if position == 0:
        llist.head = Node(1, llist.head)
    else:
        currentPosition = 0
        currentNode = llist.head 

        while currentNode:
            if currentPosition == position - 1: 
                currentNode.nextNode = Node(data, nextNode=currentNode.nextNode)

            currentNode = currentNode.nextNode
            currentPosition += 1

    llist.printLinkedList()
