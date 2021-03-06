class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

    def getData(self): return self.value

    def getNext(self): return self.pointer

    def setData(self, newdata): self.value = newdata

    def setNext(self, newpointer): self.pointer = newpointer


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end = " ")
            node = node.pointer
        print()

    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None

    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail: self.tail.pointer = node
        self.tail = node

    def _addNode(self, value):
        if not self.head: self._addFirst(value)
        else: self._add(value)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value: found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        if not self.head or not self.head.pointer: self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else: prev.pointer = node.pointer
            else:
                print("인덱스 {0}에 해당하는 노드 없음".format(index))

    def deleteNodeByValue(self, value):
        if not self.head or not self.head.pointer: self._deleteFirst(value)
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else: prev.pointer = node.pointer
            else:
                print("값 {0}에 해당되는 노드 없음".format(value))


if __name__ == "__main__":
    ll = LinkedListFIFO()
    for i in range(1, 5): ll._addNode(i)
    ll._printList()
    ll._addNode(15)
    ll.deleteNode(2)
    ll.deleteNodeByValue(4)

    ll._printList()