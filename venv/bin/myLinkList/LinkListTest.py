from LinkList import *


node = Node(100)
sll = SingleLinkList()
sll.add(0)
sll.add(0)
sll.travel()


for i in range(5):
    sll.append(i)

print("is_empty:", sll.is_empty())
print("length:", sll.length())
sll.travel()
sll.add(-1)
sll.add(0)
sll.append(0)
sll.travel()
sll.insert(sll.length(), 50)
sll.append(0)
sll.insert(3, 0)
sll.travel()
print(sll.search(500))
sll.remove(0)
sll.travel()
print("================")
sll.reverse()
sll.travel()