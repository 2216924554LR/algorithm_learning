class CycleNode:
    """singly linked list node"""
    def __init__(self, value):
        self.value = value
        self.next = None

# head_node -> node1 -> node2 -> ... -> None
class SingleLinkList:
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        if self.is_empty():
            return count
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count + 1


    def travel(self):
        cur = self.__head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
            if cur is self.__head:
                break
        print('')

    # add item at head
    def add(self, item):
        node = CycleNode(item)
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        self.__head = node

    # append item at end
    def append(self, item):
        node = CycleNode(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos > self.length():
            print("Out of index")
        else:
            cur = self.__head
            if pos == 0:
                self.add(item)
            else:
                node = CycleNode(item)
                for i in range(pos-1):
                    cur = cur.next
                cur.next, node.next = node, cur.next

    # def remove(self, item):
    #     if self.search(item):
    #         cur, pre = self.__head, None
    #         while cur:
    #             if cur.value == item:
    #                 if pre is None:
    #                     self.__head = cur.next
    #                     if cur.next is None:
    #                         return
    #                     else:
    #                         cur, pre = self.__head, None
    #                 else:
    #                     pre.next, cur = cur.next, cur.next
    #             else:
    #                 pre = cur
    #                 cur = cur.next
    #     else:
    #         print("This item not in the list")

    def search(self, item):
        if self.length():
            cur = self.__head
            while cur:
                if cur.value == item:
                    return True
                cur = cur.next
                if cur is self.__head:
                    break
        else:
            return False
        return  False

    # def reverse(self):
    #     cur = self.__head
    #     pre = None
    #     while cur:
    #         self.__head = cur
    #         cur.next, pre, cur  = pre, cur, cur.next



