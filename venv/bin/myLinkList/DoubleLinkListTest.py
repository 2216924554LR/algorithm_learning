from DoubleLinkList import *

node = DoubleNode(100)

dll = DoubleLinkList()
dll.add(50)

for i in range(5):
    dll.append(i)

dll.insert(3, 666)
dll.insert(0, 666)
dll.remove(666)
dll.travel()
dll.reverse()

dll.travel()
print("===================")
dll.reverseTravel()
