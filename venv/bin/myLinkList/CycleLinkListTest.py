from CycleLinkList import *

sll = SingleLinkList()


for i in range(5):
    sll.append(i)

sll.insert(3, 666)
sll.add(555)
sll.travel()
print(sll.length())