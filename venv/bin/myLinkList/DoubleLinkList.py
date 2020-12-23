class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkList:
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        cur = self.__head
        if self.is_empty():
            print("This is an empty list")
        else:
            while cur:
                print(cur.value, end=" ")
                cur = cur.next
            print('')

    def reverseTravel(self):
        cur = self.__head
        if self.is_empty():
            print("This is an empty list")
        else:
            while cur.next:
                cur = cur.next
            while cur:
                print(cur.value, end=" ")
                cur = cur.prev
            print('')

    # add item at head
    def add(self, item):
        node = DoubleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            self.__head.prev, node.next, self.__head = node, self.__head, node


    # append item at end
    def append(self, item):
        node = DoubleNode(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next, node.prev = node, cur


    def insert(self, pos, item):
        if pos > self.length():
            print("Out of index")
        else:
            cur = self.__head
            if pos == 0:
                self.add(item)
            else:
                node = DoubleNode(item)
                for i in range(pos-1):
                    cur = cur.next
                cur.next.prev, node.next, node.prev, cur.next = node, cur.next, cur, node


    def remove(self, item):
        if self.search(item):
            cur = self.__head
            while cur:
                if cur.value == item:
                    if cur.prev and cur.next:
                        cur.prev.next, cur.next.prev = cur.next, cur.prev
                    elif cur.prev is None and cur.next is not None:
                        self.__head, cur.next.prev = cur.next, None
                    elif cur.prev is not None and cur.next is None:
                        cur.prev.next = None
                    else:
                        self.__head = None
                cur = cur.next
        else:
            print("This item not in the list")

    def search(self, item):
        if self.length():
            cur = self.__head
            while cur:
                if cur.value == item:
                    return True
                cur = cur.next
        else:
            return False
        return  False

    def reverse(self):
        cur = self.__head
        while cur:
            cur.prev, cur.next = cur.next, cur.prev
            self.__head = cur
            cur = cur.prev





